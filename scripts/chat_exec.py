"""Spider Test Suite Execution Accuracy metric."""
import json
from typing import Any, Dict, List, Optional
from third_party.test_suite_sql_eval import evaluation as test_suite_evaluation


def compute_test_suite_metric(predictions: List[str], references: List[Dict[str, Any]], db_dir: Optional[str] = None) -> Dict[str, Any]:
    if db_dir is None:
        db_dir = references[0]["db_path"]

    foreign_key_maps = dict()
    for reference in references:
        if reference["db_id"] not in foreign_key_maps:
            foreign_key_maps[reference["db_id"]] = test_suite_evaluation.build_foreign_key_map(
                {
                    "table_names_original": reference["db_table_names"],
                    "column_names_original": [(c["table_id"], c["column_name"]) for c in reference["db_column_names"]],
                    "foreign_keys": [(fk["column_id"], fk["other_column_id"]) for fk in reference["db_foreign_keys"]],
                }
            )
    evaluator = test_suite_evaluation.Evaluator(
        db_dir=db_dir,
        kmaps=foreign_key_maps,
        etype="exec",
        plug_value=False,
        keep_distinct=False,
        progress_bar_for_each_datapoint=False,
    )

    turn_scores = {"exec": [], "exact": []}
    ## create list to save (wrong) predictions
    # wrong_result=[]
    # result=[]
    for prediction, reference in zip(predictions, references):
        try:
            e = evaluator.evaluate_one(
                reference["db_id"],
                reference["query"],
                prediction,
                turn_scores,
                idx=0,
            )
            ## add wrong predictions
            # if e['exec']!=1:
            #     wrong_example={'question':reference['question'], 'goldSQL':reference['query'], 'predictSQL':prediction}
            #     wrong_result.append(wrong_example)
            # ## add all predictions
            # example_result={'question':reference['question'], 'goldSQL':reference['query'], 'predictSQL':prediction, 'exec':e['exec']}
            # result.append(example_result)

        except AssertionError:
            pass
    evaluator.finalize()

    ## save (wrong) predictions
    # with open("casestudy/wrong_result_gpt_3.5_style.json", 'w') as file:
    #     json.dump(wrong_result, file,indent=4)
    # with open("casestudy/result_gpt_3.5_style.json", 'w') as file:
    #     json.dump(result, file,indent=4)

    return {
        "exec": evaluator.scores["all"]["exec"],
    }


### example
predictions=[]
references=[]


with open("investigation/predictions_spider_davinci_temper_20.json", 'r') as file: # predictions_gpt_3.5_turbo, predictions_text_davinci_003
    predictions = json.load(file)

with open("data/spider/examples.json", 'r') as file:
    references = json.load(file)

# predictions=['SELECT song_name, song_release_year FROM singer WHERE age = (SELECT MIN(age) FROM singer)']
# references=[references[6]]

print(len(predictions), len(references))

# Compute the execution match metric
execution_match_metric = compute_test_suite_metric(predictions, references[0:200])
# Print the result
print(execution_match_metric)


## idea: investigate the influence of prompts
## use promptes iteratively to improve the performance of the model
## inspiration: mitigate the gap between human and mechines
## multiple turn; different difficuties; different prompts; different temperatures


########### Spider ###########
## gpt_3.5_turbo_v2 {'exec': 0.6924564796905223}
## gpt_3.5_turbo_ex {'exec': 0.7137330754352031}
## gpt_3.5_turbo_ex_2 {'exec': 0.7137330754352031}

## text_davinci_003 {'exec': 0.5560928433268859}
## text_davinci_002 {'exec': 0.12475822050290135}

########### Spider-syn ###########
## gpt_3.5_turbo: {'exec': 0.6170212765957447}
## text_davinci_003: {'exec': 0.4332688588007737}

########### Spider-dk ###########
## gpt_3.5_turbo: {'exec': 0.5906542056074766}
## text_davinci_003: {'exec': 0.5383177570093458}

########### Spider-real ###########
## gpt_3.5_turbo: {'exec': 0.6456692913385826}
## text_davinci_003: {'exec': 0.5196850393700787}

########### Dr.Spider ###########
## db_content_equivalence: {'exec': 0.418848167539267}
## db_schema_abbreviation: {'exec': 0.6400280406589555}
## db_schema_synonym: {'exec': 0.5368461244749905}
## nlq_column_attribute: {'exec': 0.6134453781512605}
## nlq_column_carrier: {'exec': 0.6735751295336787}
## nlq_column_synonym: {'exec': 0.47424511545293074}
## nlq_column_value: {'exec': 0.5625}
## nlq_keyword_carrier: {'exec': 0.7844611528822055}
## nlq_keyword_synonym: {'exec': 0.5760755508919203}
## nlq_multitype: {'exec': 0.5292376017764618}
## nlq_others: {'exec': 0.6512947853848883}
## nlq_value_synonym: {'exec': 0.4624505928853755}
## sql_comparison: {'exec': 0.6910112359550562}
## sql_db_number: {'exec': 0.7707317073170732}
## sql_db_text: {'exec': 0.6553238199780461}
## sql_nondb_number: {'exec': 0.8931297709923665}
## sql_sort_order: {'exec': 0.609375}

########### typo ###########
## gpt_3.5_turbo: {'exec': 0.648936170212766}

########### style ###########
## gpt_3.5_turbo: {'exec': 0.6450676982591876}
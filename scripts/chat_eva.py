import json
from typing import Dict, Any
from third_party.spider.evaluation import Evaluator, build_foreign_key_map

def compute_exact_match_metric(predictions, references) -> Dict[str, Any]:
    foreign_key_maps = dict()
    for reference in references:
        if reference["db_id"] not in foreign_key_maps:
            foreign_key_maps[reference["db_id"]] = build_foreign_key_map(
                {
                    "table_names_original": reference["db_table_names"],
                    "column_names_original": [(c["table_id"], c["column_name"]) for c in reference["db_column_names"]],
                    "foreign_keys": [(fk["column_id"], fk["other_column_id"]) for fk in reference["db_foreign_keys"]],
                }
            )
    evaluator = Evaluator(references[0]["db_path"], foreign_key_maps, "match")
    for prediction, reference in zip(predictions, references):
        turn_idx = reference.get("turn_idx", 0)
        # skip final utterance-query pairs
        if turn_idx < 0:
            continue
        _ = evaluator.evaluate_one(reference["db_id"], reference["query"], prediction)
    evaluator.finalize()
    return {
        "exact_match": evaluator.scores["all"]["exact"],
    }

### example
predictions=[]
references=[]

## extend example
# with open("data/spider/predictions_gpt_3.5_turbo_v2_2.json", 'r') as file:
#     predictions_2 = json.load(file)
# predictions.extend(predictions_2)

# with open("data/spider/predictions_gpt_3.5_turbo_v2.json", "w", encoding="utf-8") as f:
#     json.dump(predictions, f, ensure_ascii=False,indent=4)


with open("data/diagnostic-robustness-text-to-sql/data/NLQ_value_synonym/predictions_gpt_3.5_turbo_nlq_value_synonym.json", 'r') as file: # predictions_gpt_3.5_turbo, predictions_text_davinci_003
    predictions = json.load(file)

with open("data/diagnostic-robustness-text-to-sql/data/NLQ_value_synonym/examples.json", 'r') as file:
    references = json.load(file)

print(len(predictions), len(references))
      
# Compute the exact match metric
exact_match_metric = compute_exact_match_metric(predictions, references)
# Print the result
print(exact_match_metric)


########### Spider ###########
## gpt_3.5_turbo_v2: {'exact_match': 0.40425531914893614}
## gpt_3.5_turbo_ex: {'exact_match': 0.4661508704061896}
## gpt_3.5_turbo_ex_2: {'exact_match': 0.4661508704061896}

## text_davinci_003: {'exact_match': 0.3191489361702128}
## text_davinci_002:{'exact_match': 0.059961315280464215}

########### Spider-syn ###########
## gpt_3.5_turbo: {'exact_match': 0.38781431334622823}
## text_davinci_003: {'exact_match': 0.22823984526112184}

########### Spider-dk ###########
## gpt_3.5_turbo: {'exact_match': 0.41495327102803736}
## text_davinci_003: {'exact_match': 0.30654205607476637}

########### Spider-real ###########
## gpt_3.5_turbo: {'exact_match': 0.41141732283464566}
## text_davinci_003: {'exact_match': 0.30708661417322836}

########### Dr.Spider ###########
## db_content_equivalence: {'exact_match': 0.31413612565445026}
## db_schema_abbreviation: {'exact_match': 0.3866105853487557}
## db_schema_synonym: {'exact_match': 0.31691485299732725}
## nlq_column_attribute: {'exact_match': 0.40336134453781514}
## nlq_column_carrier: {'exact_match': 0.4697754749568221}
## nlq_column_synonym: {'exact_match': 0.3463587921847247}
## nlq_column_value: {'exact_match': 0.3782894736842105}
## nlq_keyword_carrier: {'exact_match': 0.49624060150375937}
## nlq_keyword_synonym: {'exact_match': 0.30325288562434416}
## nlq_multitype: {'exact_match': 0.38786084381939306}
## nlq_others: {'exact_match': 0.4228449804895353}
## nlq_value_synonym: {'exact_match': 0.4189723320158103}
## sql_comparison: {'exact_match': 0.3146067415730337}
## sql_db_number: {'exact_match': 0.624390243902439}
## sql_db_text: {'exact_match': 0.4039517014270033}
## sql_nondb_number: {'exact_match': 0.5419847328244275}
## sql_sort_order: {'exact_match': 0.34375}




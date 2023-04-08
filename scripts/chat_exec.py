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
    for prediction, reference in zip(predictions, references):
        try:
            _ = evaluator.evaluate_one(
                reference["db_id"],
                reference["query"],
                prediction,
                turn_scores,
                idx=0,
            )
        except AssertionError:
            pass
    evaluator.finalize()

    return {
        "exec": evaluator.scores["all"]["exec"],
    }

### example
predictions=[]
references=[]
with open("data/spider/predictions_text_davinci_002.json", 'r') as file:
    predictions = json.load(file)

with open("data/spider/examples.json", 'r') as file:
    references = json.load(file)
      
# Compute the exact match metric
execution_match_metric = compute_test_suite_metric(predictions, references)
# Print the result
print(execution_match_metric)

## gpt_3.5_turbo_v2 {'exec': 0.6924564796905223}
## gpt_3.5_turbo_ex {'exec': 0.7137330754352031}
## gpt_3.5_turbo_ex_2 {'exec': 0.7137330754352031}

## text_davinci_003 {'exec': 0.44197292069632493}
## text_davinci_002 {'exec': 0.12475822050290135}

## idea: investigate the influence of prompts
## use promptes iteratively to improve the performance of the model
## inspiration: mitigate the gap between human and mechines
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
with open("data/spider/predictions_gpt_3.5_turbo.json", 'r') as file:
    predictions = json.load(file)

with open("data/spider/examples.json", 'r') as file:
    references = json.load(file)

# Compute the exact match metric
exact_match_metric = compute_exact_match_metric(predictions, references[0:20])

# Print the result
print(exact_match_metric)
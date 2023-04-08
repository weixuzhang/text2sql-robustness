from chat_process import *

#spider 
# data_filepath = "data/spider/dev.json"
# db_path = "database"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/spider/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/spider/formatted_spider_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/spider/serialized_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# processed_examples = [spider_add_serialized_schema_withnl(example) for example in examples]
# with open("data/spider/processed_data.json", "w", encoding="utf-8") as f:
#     json.dump(processed_examples, f, ensure_ascii=False,indent=4)

# serialized_examples=[spider_add_serialized_schema(example) for example in examples]
# with open("data/spider/serialized_data.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples, f, ensure_ascii=False,indent=4)

###################################################

##spider-syn

# data_filepath = "data/spider-syn/dev_syn.json"
# db_path = "database"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/spider-syn/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/spider-syn/formatted_spider_syn_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/spider-syn/serialized_syn_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)


## spider-realistic
# data_filepath = "data/spider-realistic/spider-realistic.json"
# db_path = "database"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/spider-realistic/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/spider-realistic/formatted_spider_real_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/spider-realistic/serialized_real_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)


## spider-dk
data_filepath = "data/spider-dk/Spider-DK.json"
db_path = "data/spider-dk/database"

examples=generate_examples_lst(data_filepath, db_path)
with open("data/spider-dk/examples.json", "w") as out_file:
    json.dump(examples, out_file,indent=4)

formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
with open("data/spider-dk/formatted_spider_dk_data.json", "w", encoding="utf-8") as f:
    json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
with open("data/spider-dk/serialized_dk_data_str.json", "w", encoding="utf-8") as f:
    json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)
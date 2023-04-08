from chat_process import *


################################## spider ##################################
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

# print(len(examples)) # 1034

# processed_examples = [spider_add_serialized_schema_withnl(example) for example in examples]
# with open("data/spider/processed_data.json", "w", encoding="utf-8") as f:
#     json.dump(processed_examples, f, ensure_ascii=False,indent=4)

# serialized_examples=[spider_add_serialized_schema(example) for example in examples]
# with open("data/spider/serialized_data.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples, f, ensure_ascii=False,indent=4)



################################## spider-syn ##################################

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

# print(len(examples)) # 1034

################################## spider-realistic ##################################

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

# print(len(examples)) # 508

################################## spider-dk ##################################

# data_filepath = "data/spider-dk/Spider-DK.json"
# db_path = "data/spider-dk/database"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/spider-dk/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/spider-dk/formatted_spider_dk_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/spider-dk/serialized_dk_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 535

################################## dr.spider_db_content_equivalence ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/DB_DBcontent_equivalence/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/DB_DBcontent_equivalence/database_post_perturbation"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/DB_DBcontent_equivalence/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/DB_DBcontent_equivalence/formatted_spider_dr_db_content_equivalence_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/DB_DBcontent_equivalence/serialized_dr_db_content_equivalence_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 382

################################## dr.spider_db_schema_abbreviation ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/DB_schema_abbreviation/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/DB_schema_abbreviation/database_post_perturbation"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/DB_schema_abbreviation/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/DB_schema_abbreviation/formatted_spider_dr_db_schema_abbreviation_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/DB_schema_abbreviation/serialized_dr_db_schema_abbreviation_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 2853

################################## dr.spider_db_schema_synonym ##################################

data_filepath = "data/diagnostic-robustness-text-to-sql/data/DB_schema_synonym/questions_post_perturbation.json"
db_path = "data/diagnostic-robustness-text-to-sql/data/DB_schema_synonym/database_post_perturbation"

examples=generate_examples_lst(data_filepath, db_path)
with open("data/diagnostic-robustness-text-to-sql/data/DB_schema_synonym/examples.json", "w") as out_file:
    json.dump(examples, out_file,indent=4)

formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
with open("data/diagnostic-robustness-text-to-sql/data/DB_schema_synonym/formatted_spider_dr_db_schema_synonym_data.json", "w", encoding="utf-8") as f:
    json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
with open("data/diagnostic-robustness-text-to-sql/data/DB_schema_synonym/serialized_dr_db_schema_synonym_data_str.json", "w", encoding="utf-8") as f:
    json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

print(len(examples)) # 2619

################################## dr.spider_nlq_column_attribute ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/NLQ_column_attribute/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/NLQ_column_attribute/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_attribute/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_attribute/formatted_spider_dr_nlq_column_attribute_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_attribute/serialized_dr_nlq_column_attribute_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 119

################################## dr.spider_nlq_column_carrier ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/NLQ_column_carrier/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/NLQ_column_carrier/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_carrier/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_carrier/formatted_spider_dr_nlq_column_carrier_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_carrier/serialized_dr_nlq_column_carrier_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 579

################################## dr.spider_nlq_column_synonym ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/NLQ_column_synonym/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/NLQ_column_synonym/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_synonym/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_synonym/formatted_spider_dr_nlq_column_synonym_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_synonym/serialized_dr_nlq_column_synonym_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 563

################################## dr.spider_nlq_column_value ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/NLQ_column_value/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/NLQ_column_value/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_value/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_value/formatted_spider_dr_nlq_column_value_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_column_value/serialized_dr_nlq_column_value_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 304

################################## dr.spider_nlq_keyword_carrier ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_carrier/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_carrier/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_carrier/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_carrier/formatted_spider_dr_nlq_keyword_carrier_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_carrier/serialized_dr_nlq_keyword_carrier_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 399

################################## dr.spider_nlq_keyword_synonym ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_synonym/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_synonym/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_synonym/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_synonym/formatted_spider_dr_nlq_keyword_synonym_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_keyword_synonym/serialized_dr_nlq_keyword_synonym_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 953

################################## dr.spider_nlq_multitype ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/NLQ_multitype/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/NLQ_multitype/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_multitype/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_multitype/formatted_spider_dr_nlq_multitype_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_multitype/serialized_dr_nlq_multitype_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 1351

################################## dr.spider_nlq_others ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/NLQ_others/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/NLQ_others/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_others/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_others/formatted_spider_dr_nlq_others_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_others/serialized_dr_nlq_others_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 2819

################################## dr.spider_nlq_value_synonym ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/NLQ_value_synonym/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/NLQ_value_synonym/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_value_synonym/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_value_synonym/formatted_spider_dr_nlq_value_synonym_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/NLQ_value_synonym/serialized_dr_nlq_value_synonym_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 506

################################## dr.spider_sql_comparison ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/SQL_comparison/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/SQL_comparison/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_comparison/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_comparison/formatted_spider_dr_sql_comparison_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_comparison/serialized_dr_sql_comparison_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 178

################################## dr.spider_sql_db_number ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/SQL_DB_number/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/SQL_DB_number/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_DB_number/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_DB_number/formatted_spider_dr_sql_db_number_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_DB_number/serialized_dr_sql_db_number_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 410

################################## dr.spider_sql_db_text ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/SQL_DB_text/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/SQL_DB_text/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_DB_text/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_DB_text/formatted_spider_dr_sql_db_text_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_DB_text/serialized_dr_sql_db_text_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 911

################################## dr.spider_sql_nondb_number ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/SQL_NonDB_number/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/SQL_NonDB_number/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_NonDB_number/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_NonDB_number/formatted_spider_dr_sql_nondb_number_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_NonDB_number/serialized_dr_sql_nondb_number_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 131

################################## dr.spider_sql_sort_order ##################################

# data_filepath = "data/diagnostic-robustness-text-to-sql/data/SQL_sort_order/questions_post_perturbation.json"
# db_path = "data/diagnostic-robustness-text-to-sql/data/SQL_sort_order/databases"

# examples=generate_examples_lst(data_filepath, db_path)
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_sort_order/examples.json", "w") as out_file:
#     json.dump(examples, out_file,indent=4)

# formatted_examples = [spider_pre_process_one_function(example, True) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_sort_order/formatted_spider_dr_sql_sort_order_data.json", "w", encoding="utf-8") as f:
#     json.dump(formatted_examples, f, ensure_ascii=False,indent=4)

# serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
# with open("data/diagnostic-robustness-text-to-sql/data/SQL_sort_order/serialized_dr_sql_sort_order_data_str.json", "w", encoding="utf-8") as f:
#     json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

# print(len(examples)) # 192


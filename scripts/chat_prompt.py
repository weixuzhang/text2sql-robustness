import json
import random
from chat_process import *

### CREATE TABLE format
def example_to_create_table(example):
    tables = example['db_table_names']
    columns = example['db_column_names']
    types = example['db_column_types']
    primary_keys = example['db_primary_keys']
    foreign_keys = example['db_foreign_keys']
    question = example['question']

    create_table_commands = ''
    for table_id, table_name in enumerate(tables):
        columns_for_table = [col for col in columns if col['table_id'] == table_id]
        types_for_table = [type for i, type in enumerate(types) if columns[i]['table_id'] == table_id]
        primary_keys_for_table=[pk['column_id'] for pk in primary_keys if columns[pk['column_id']]['table_id'] == table_id]
        column_primary_keys = [columns[pk]['column_name'] for pk in primary_keys_for_table]
        foreign_keys_for_table = [(fk["column_id"], fk["other_column_id"]) for fk in foreign_keys if columns[fk['column_id']]['table_id'] == table_id]
        table_foreign_keys=[]
        if len(foreign_keys_for_table) > 0:
            table_foreign_keys = [(columns[fk[0]]['column_name'], columns[fk[1]]['column_name'], tables[columns[fk[1]]['table_id']]) for fk in foreign_keys_for_table]
        # Generate the column definitions
        column_definitions = ', '.join(['{} {}'.format(column['column_name'], data_type) for column, data_type in zip(columns_for_table, types_for_table)])
        # Add primary key constraint
        if len(column_primary_keys) > 0:
            primary_key_constraint = ', '.join(['PRIMARY KEY({})'.format(pk) for pk in column_primary_keys])
            column_definitions += ', ' + primary_key_constraint
        # Add foreign key constraint
        if len(table_foreign_keys) > 0:
            for fk in table_foreign_keys:
                foreign_key_constraint = 'FOREIGN KEY ({}) REFERENCES {}({})'.format(fk[0], fk[2],fk[1])
                column_definitions += ', ' + foreign_key_constraint

        create_table_command = 'CREATE TABLE {} ({})'.format(table_name, column_definitions)
        create_table_commands=create_table_commands+create_table_command+' \n '
        
    # Create the final dictionary
    result_dict = {
        'question': question,
        'create_table_commands': create_table_commands,
    }
    
    return result_dict  

### API DOC format
def example_to_api_doc(example):
    tables = example['db_table_names']
    columns = example['db_column_names']
    question = example['question']

    prompts = '### Postgres SQL tables, with their properties:\n#'
    for table_id, table_name in enumerate(tables):
        columns_for_table = [col for col in columns if col['table_id'] == table_id]
        column_definitions = ', '.join(['{}'.format(column['column_name']) for column in columns_for_table ])
        table_schema = '\n# {} ({})'.format(table_name, column_definitions)
        prompts=prompts+table_schema

    prompts=prompts+ "\n#\n###"+question+"\nSELECT"  

    return prompts 

### one shot format
def one_short(example, train_examples):
    question_schema = spider_add_serialized_schema_str(example)
    random.seed(42)
    random.shuffle(train_examples)
    serialized_one_examples_str=spider_add_serialized_schema_str(train_examples[0])
    example_str='Here is an examples including input and output:\n'
    example_str=example_str+" input: " +serialized_one_examples_str+ " output: "+ train_examples[0]['query']+ "\n"
    example_str=example_str+" Now please use valid SQLite to answer the following questions: "+ question_schema
    return example_str


### 5 shot format
def five_short(example, train_examples):
    question_schema = spider_add_serialized_schema_str(example)
    random.seed(42)
    random.shuffle(train_examples)
    serialized_5_examples_str=[spider_add_serialized_schema_str(example) for example in train_examples[0:5]]
    example_str='Here are 5 examples including input and output:\n'
    for i in range(5):
        example_str=example_str+" input: " +serialized_5_examples_str[i]+ " output: "+ train_examples[i]['query']+ "\n"
    example_str=example_str+" Now please use valid SQLite to answer the following questions: "+ question_schema
    return example_str



### Generate examples in CREATE TABLE format
data_filepath = "data/spider/dev.json"
db_path = "database"
examples=generate_examples_lst(data_filepath, db_path)

example_to_create_table_dic=[example_to_create_table(example) for example in examples]
serialized_examples_str = ["question: "+ d['question'] +" create_table_commands: " + d['create_table_commands'] for d in example_to_create_table_dic]
with open("investigation/serialized_create_command.json", "w", encoding="utf-8") as f:
    json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)

### generate examples in API DOC format
serialized_api_doc = [example_to_api_doc(example) for example in examples]
with open("investigation/serialized_api_doc.json", "w", encoding="utf-8") as f:
    json.dump(serialized_api_doc, f, ensure_ascii=False,indent=4)


### generate examples in QUESTION format
question = [example['question'] for example in examples]
with open("investigation/serialized_question.json", "w", encoding="utf-8") as f:
    json.dump(question, f, ensure_ascii=False,indent=4)


### generate examples in SCHEMA format
serialized_examples_str=[spider_add_serialized_schema_str(example) for example in examples]
with open("investigation/serialized_schema.json", "w", encoding="utf-8") as f:
    json.dump(serialized_examples_str, f, ensure_ascii=False,indent=4)


### generate examples in one-shot format
train_examples=generate_examples_lst("data/spider/train_spider.json", db_path)
serialized_one_shot = [one_short(example,train_examples) for example in examples]
with open("investigation/serialized_one_shot.json", "w", encoding="utf-8") as f:
    json.dump(serialized_one_shot, f, ensure_ascii=False,indent=4)


### generate examples in 5-shot format
train_examples=generate_examples_lst("data/spider/train_spider.json", db_path)
serialized_5_shots = [five_short(example,train_examples) for example in examples]
with open("investigation/serialized_5shot.json", "w", encoding="utf-8") as f:
    json.dump(serialized_5_shots, f, ensure_ascii=False,indent=4)

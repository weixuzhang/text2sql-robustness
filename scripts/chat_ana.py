import json

with open("casestudy/result_gpt_3.5_ex.json", 'r') as file: 
    result_ex = json.load(file)
with open("casestudy/result_gpt_3.5_syn.json", 'r') as file: 
    result_syn = json.load(file)

with open("data/spider/perturbation_spider_typo.json", 'r') as file: 
    question_typo = json.load(file)
with open("casestudy/result_gpt_3.5_typo.json", 'r') as file: 
    result_typo = json.load(file)
for i in range(len(result_typo)):
    result_typo[i]['question']=question_typo[i]

with open("data/spider/perturbation_spider_style.json", 'r') as file: 
    question_style = json.load(file)
with open("casestudy/result_gpt_3.5_style.json", 'r') as file: 
    result_style = json.load(file)
for i in range(len(result_style)):
    result_style[i]['question']=question_style[i]

casestudy=[]
for i in range(len(result_ex)):
    if result_ex[i]['exec']==1 and result_typo[i]['exec']!=1 and result_syn[i]['exec']!=1 and result_style[i]['exec']!=1: #
        casestudy.append({
            "id": i,
            "ex": result_ex[i],
            "typo": result_typo[i],
            "syn": result_syn[i],  
            "style": result_style[i],
        })

with open("casestudy/casestudy.json", 'w') as file:
    json.dump(casestudy, file,indent=4)
print(len(casestudy))
import json
with open(file = "mysqldata.json", encoding='utf8') as f:
    data = json.load(f)

data = data['RECORDS']

def unique(data: list):
    """
    对于输入的列表，返回一个去重的列表。区别于set函数，主要针对unhashable的数据类型
    """
    temp = []
    for item in data:
        if not item in temp:
            temp.append(item)
    return temp


returned_data = {
    "nodes": [],
    "links": []
}

for item in data:
    returned_data["nodes"].append({'name':item['ST1'],'category':item['ST1LX'],'highlight':0, 'detail':1})
    returned_data["nodes"].append({'name': item['ST2'], 'category': item['ST2LX'], 'highlight': 0, 'detail': 1})
    returned_data["links"].append({'source':item['ST1'], 'target':item['ST2'], 'name':item['GXLX']})

returned_data['nodes'] = unique(returned_data['nodes'])
returned_data['links'] = unique(returned_data['links'])

with open("graphdata.json","w",encoding='utf8') as f2:
    json.dump(returned_data,f2, ensure_ascii=False)

with open("graphdata.json","r",encoding='utf8') as f3:
    data1 = json.load(f3)

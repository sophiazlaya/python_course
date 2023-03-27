import json

with open('wikidata_1000.json', 'r', encoding='utf-8') as a:
    lines = a.readlines()
    dictt = {}
    for line in lines:
        json_line = json.loads(line)
        try:
            word = json_line["label"]["value"]
            description = json_line["description"]["value"]
            dictt[word] = description
        except KeyError:
            continue

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(dictt, f, ensure_ascii=False, indent=4)








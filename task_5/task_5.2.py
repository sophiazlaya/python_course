
import json
import collections

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as a:
    data = json.load(a)

characters = collections.defaultdict(list)
for act in data['acts']:
    for scene in act['scenes']:
        for action in scene['action']:
            for i in action['says']:
                characters[action['character']].append(i)

with open('replics.json', 'w') as w:
    json.dump(characters, w, ensure_ascii=False, indent=4)
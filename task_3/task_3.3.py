import json
import collections


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as d:
    data = json.load(d)
mean = collections.Counter()
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                mean[action['character']] += 1


print(mean)
"""Подсчитайте, сколько раз в корпусе слово “может” встречается как союз (CONJ), а сколько - как глагол (VERB)."""

import xml.etree.ElementTree as ET
tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

count_mb = {"VERB": 0, "CONJ": 0}

for token in root.iter('token'):
    if token.attrib["text"].lower() == 'может':
        gs = []
        for g in token.iter("g"):
            gs.append(g.attrib["v"])
        if "VERB" in gs:
            count_mb["VERB"] += 1
        elif "CONJ" in gs:
            count_mb["CONJ"] += 1


print(count_mb)

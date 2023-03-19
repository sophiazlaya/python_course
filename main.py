import xml.etree.ElementTree as ET
tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

sentences = []
for source in root.iter('source'):
    sentences.append(source.text)

print(sentences)
with open("sentences.txt", 'w', encoding='utf-8') as file:
    file.write('\n'.join(sentences))

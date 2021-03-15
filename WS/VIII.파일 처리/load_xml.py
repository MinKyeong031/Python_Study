import xml.etree.ElementTree as ET
import codecs
f= open('movie.xml', encoding='utf8')
data = f.read()
#print(data)
tree = ET.ElementTree(ET.fromstring(data))
root = tree.getroot()
#print(root.tag)
for child in root:
    print('tag : ' + child.tag + ', text : ' + child.text)
f.close()

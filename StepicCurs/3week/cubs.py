from lxml import etree
from xml.etree import ElementTree

str = input()

dict = {'red': 0, 'blue': 0, 'green': 0}
tree = ElementTree.fromstring(str)
root = etree.getroot()

print(root)
from xml.etree import ElementTree

tree = ElementTree.parse('exaple.xml')
root = tree.getroot()

def childrens(root):
    for child in root:
        print(child.tag,child.text)
        childrens(child)


childrens(root)

tree.write('exaMple_copy.xml')

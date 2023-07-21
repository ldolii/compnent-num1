import numpy as np
import os
import json
from PIL import Image
from lxml import etree as ET
from lxml import etree 

root = ET.Element('bookstore')

book1 = ET.Element('book', {'id': '001'})
title1 = ET.Element('title')
title1.text = 'Python for Beginners'
author1 = ET.Element('author')
author1.text = 'John Smith'
year1 = ET.Element('year')
year1.text = '2019'

book1.append(title1)
book1.append(author1)
book1.append(year1)

root.append(book1)


book2 = ET.Element('book', {'id': '002'})
title2 = ET.Element('title')
title2.text = 'Advanced Python'
author2 = ET.Element('author')
author2.text = 'Jane Doe'
year2 = ET.Element('year')
year2.text = '2020'

book2.append(title2)
book2.append(author2)
book2.append(year2)

root.append(book2)

tree = ET.ElementTree(root)
tree.write('books.xml',encoding='utf-8', xml_declaration=True)

# READ  LDO
xml_path = "./books.xml"
if os.path.exists(xml_path) is False:
    print(f"Warning: not found '{xml_path}', skip this annotation file.")


with open(xml_path) as fid:
                xml_str = fid.read()

xml = etree.fromstring(xml_str.encode('utf-8'))

#print(xml_str)
print("done done")
print(len(xml))



def return_xml_tag_text(xml):
    print({xml.tag: xml.text})
    if len(xml) == 0:  # 遍历到底层，直接返回tag对应的信息
            #print({xml.tag: xml.text})
            return {xml.tag: xml.text}

    result = {}
    for child in xml:
        child_result = return_xml_tag_text(child)  # 递归遍历标签信息
        result[child.tag] = []
        #result[child.tag].append(child_result[child.tag])
        #result.append(child_result)
        '''
        if child.tag != 'object':
            result[child.tag] = child_result[child.tag]
        else:
            if child.tag not in result:  # 因为object可能有多个，所以需要放入列表里
                result[child.tag] = []
            result[child.tag].append(child_result[child.tag])
            '''
    #return {xml.tag: result}
    return child_result


xml_list = return_xml_tag_text(xml)
#print(xml_list)

'''
for child in xml:
    print(len(child))
    print(child.tag)
    print(child.text)
    for child1 in child:
        print(len(child1))
        print(child1.tag)
        print(child1.text)
'''    
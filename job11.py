import xml.etree.ElementTree as ET
xmlfile = 'domains.xml'
mytree = ET.parse(xmlfile)
myroot = mytree.getroot()

Name_attribute = "domain"

NO_node = 0
for elm in myroot.findall(".//"):
    if elm.get('name') == Name_attribute:
        NO_node+=1;
print ("Nombre total de l'attribut domain : ", NO_node)
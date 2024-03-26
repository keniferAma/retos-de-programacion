"""/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */"""

import json

address = "C:\\Users\\kenifer\\OneDrive\\Documentos\\documento-reto-json-xml.txt"
information = {'nombre': 'alejandro', 'apellido': 'velez', 'estado civil': 'casado',
               'lenguages de programacion': ['python', 'javascript', 'java', 'kotlin', 'rust', 'go']
               }


# json #

with open(address, "w") as file:
    json.dump(information, file)


with open(address) as file:
    result = json.load(file)

print(result)


"""'r': This mode is used for reading from an existing file. If the file does not exist, it raises an IOError exception.
-'w': This mode is used for writing to a file. If the file exists, it truncates the file. 
If the file does not exist, it creates a new file.
-'a': This mode is used for appending to a file. If the file exists, the new data being written is automatically 
added to the end. If the file does not exist, it creates a new file.
-'r+': This mode is used for both reading and writing from a file. The file pointer placed at the beginning of 
the file.
-'w+': This mode is used for both writing and reading from a file. Overwrites the existing file if the file exists. 
If the file does not exist, it creates a new file for reading and writing.
-'a+': This mode is used for both appending and reading from a file. The file pointer is at the 
end of the file if the file exists. The file opens in the append mode. If the file does not exist, 
it creates a new file for reading and writing."""

"""REMEMBER: Json supports strings. numbers, booleans, null, arrays, objects"""



# xml #

import xml.etree.ElementTree as ET

tree = ET.parse('C:\\Users\\kenifer\\OneDrive\\Documentos\\xml-file.xml')
root = tree.getroot()

print(len(root))
print(root.tag)
"""1
data""" # Getting the tag information
print(root[0].text)
"""General document Information"""

print(len(root[0][0].tag))
"""4"""

print(root[0][0].text)
"""User information"""

print(root[0][0].tag)
"""user"""

print(root[0][0].attrib)
"""{'id': '1'}""" # The attribute is the information inside the tag.

print(root.attrib)
"""{'date': '21-03-2024'}"""

print(root[0][0][1].text)
"""Hernandez"""

print(root[0][0].items())


# Looping through xml files #

for item in root.iter('name'):
    print(item.text)

"""Adolfo
alejandro
Fernando"""

print(root[0][0].findall('name')[0].text)
"""Adolfo"""

root[0][0][2].text = "34" # To replace information

print(root[0][0][2].text)
tree.write('C:\\Users\\kenifer\\OneDrive\\Documentos\\xml-file.xml') # Neccesary to make the changes in the xml file.

#root[0].remove(root[0][1]) # on this case we're removing root[0][1], the user with id=2
#tree.write('C:\\Users\\kenifer\\OneDrive\\Documentos\\xml-file.xml') 

for item in root.findall('name'):
    print(item.text)

# print the entire file #
    
xml_str = ET.tostring(root, encoding='utf8').decode('utf8')
print(xml_str)

"""<?xml version='1.0' encoding='utf8'?>
<data date="21-03-2024">
    <documentInformation>General document Information
        <user id="1">User information
            <name>Adolfo</name>
            <surname>Hernandez</surname>
            <age>34</age>
            <status>single</status>
        </user>
        <user id="2">User information
            <name>alejandro</name>
            <surname>Fernandez</surname>
            <age>21</age>
            <status>married</status>
        </user>
        <user id="3">User information
            <name>Fernando</name>
            <surname>Posada</surname>
            <age>43</age>
            <status>single</status>
        </user>
    </documentInformation>
</data>"""


# This is the same file information #
"""<data date="21-03-2024"> #ROOT
    <documentInformation>General document Information #ROOT[0]
        <user id="1">User information #ROOT[0][0]
            <name>Adolfo</name> #ROOT[0][0][0]
            <surname>Hernandez</surname> #ROOT[0][0][1]
            <age>32</age> #ROOT[0][0][2]
            <status>single</status>
        </user>
        <user id="2">User information #ROOT[0][1]
            <name>alejandro</name>
            <surname>Fernandez</surname>
            <age>21</age> #ROOT[0][1][2]
            <status>married</status>
        </user>
        <user id="3">User information
            <name>Fernando</name>
            <surname>Posada</surname>
            <age>43</age>
            <status>single</status>
        </user>
    </documentInformation>
</data>"""


# extra #

class CustomFile:
    def __init__(self, xml_path=None, json_path=None):
        self.xml_path = xml_path
        self.json_path = json_path

    def read_xml_file(self):
        if self.xml_path:
            if self.xml_path[-4:] == '.xml':
                tree = ET.parse(self.xml_path)
                root = tree.getroot()
                xml_str = ET.tostring(root, encoding='utf8').decode('utf8')

                return xml_str
            else:
                return {'Error': 'The file is not xml'}
        else:
            return {'Error': 'file not provided'}
            
    def read_json_file(self):
        if self.json_path:
            if self.xml_path[-5:] == '.json':
                with open(self.json_path, "r+") as file:
                    result = json.load(file)    

                return result
            else:
                return {'Error': 'The file is json'}
            
        else:
            return {'Error': 'File not provided'}
        
first_try = CustomFile()
print(first_try.read_xml_file)




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
import xml

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



# xml #


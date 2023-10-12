"""/*
 * Enunciado: Crea una función que sea capaz de detectar y retornar todos los
 * handles de un texto usando solamente Expresiones Regulares.
 * Debes crear una expresión regular para cada caso:
 * - Handle usuario: Los que comienzan por "@"
 * - Handle hashtag: Los que comienzan por "#"
 * - Handle web: Los que comienzan por "www.", "http://", "https://" 
 *   y finalizan con un dominio (.com, .es...)
 */"""

import re

string = "#NosEstanAcabando @ayuda por favor http://nosestanmatando.com, www.pruebas.es"
pattern = r"#[a-zA-Z]{1,}"
pattern_2 = r"@[a-zA-Z]{1,}"
pattern_3 = r"((www\.|http://|https://)[a-zA-Z0-9-]+(\.com|\.es))"

result = re.findall(pattern, string)
result_2 = re.findall(pattern_2, string)
result_3 = [match.group() for match in re.finditer(pattern_3, string)]
print(result)
print(result_2)
print(result_3)  



# Now we're gonna see the IA version:

import re

def detectar_handles(texto):
    # Expresión regular para handles de usuario
    patron_usuario = r"@\w+"
    usuarios = re.findall(patron_usuario, texto)

    # Expresión regular para handles de hashtag
    patron_hashtag = r"#\w+"
    hashtags = re.findall(patron_hashtag, texto)

    # Expresión regular para handles web
    patron_web = r"(www\.|http://|https://)[a-zA-Z0-9-]+(\.com|\.es)"
    webs = [match.group() for match in re.finditer(patron_web, texto)]

    return usuarios, hashtags, webs

# Prueba la función con un ejemplo
texto = "#NosEstanAcabando @ayuda por favor http://nosestanmatando.com"
usuarios, hashtags, webs = detectar_handles(texto)
print("Usuarios:", usuarios)
print("Hashtags:", hashtags)
print("Webs:", webs)

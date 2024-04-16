"""/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */"""

import re

string = 'ase2sor93i0a d1e personas'
pattern = r'[0-9]'
string_only = r'[a-zA-Z\s]{1,}'

concurrences = re.findall(pattern, string)
string_concurrences = re.findall(string_only, string)

print(concurrences)
print(string_concurrences)
print(''.join(string_concurrences))


# extra challenge #

# regular expression for email #

import re

email_string = 'kenifer@misena.edu'
email_pattern = r'^[\w]{3,10}@(?:misena|gmail|outlook)(?:\.edu|\.com(?:\.co)?)?$'

print(re.findall(email_pattern, email_string))

"""
about '?':

In regular expressions, the ? symbol is a quantifier that makes the preceding element optional. 
It means that the preceding element may appear zero or one time.

When you see a ? at the end of a parenthesis, it applies to the entire group within the parenthesis. 
For example, in the regular expression (abc)?, the ? makes the entire group abc optional. 
This means the regular expression will match strings that contain abc and strings that do not contain abc.
"""

"""
about non capturing ?:
import re

# Define a string and a regular expression with a non-capturing group
string = "I like cats and I like dogs."
regex = r"I like (?:cats|dogs)"  # The (?:...) defines a non-capturing group

# Use re.findall() to find all matches
matches = re.findall(regex, string)

# Print the matches
print(matches)  # Outputs: ['I like cats', 'I like dogs']
"""


match = re.match(email_pattern, 'alenadro@gmail.com')

try:
    print(match.group()) # the 'group' attribute return the matched concurrency. (works either with search and match)

except AttributeError as message:
    print(message)



# regular expression for number phone #

phone_string = '+57 3137576362'
phone_pattern = r'(\+[0-9]{2,3})?\s?[0-9]{10}'

print(re.search(phone_pattern, phone_string))
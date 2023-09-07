# ejercicios de expresiones regulares #
import re

#Encuentra todas las palabras que comiencen con la letra "a"
texto = "abelardo es una persona con muchos a agujeros de azucar"
patrón = r"[Aa][a-z]+" #no funcionó con (A|a) entonces usé secuencia [Aa]
resultado = re.findall(patrón, texto)
print(resultado)

# otra forma de hacerlo pero sin expresiones regulares. (con dificultades)
texto_lista = [] #La lista siempre debe ir en este tipo de posicion, para que me acoja todos los valores
texto = "abelardo es una persona con muchos agujeros de azucar"
for t in texto.split():
    if t.startswith("a"): # esta opcion me arroja un bool
        texto_lista.append(t)

print(texto_lista)

#Encuentra todas las palabras que terminen con la letra "s"
texto = "abelardo es una persona con muchos a agujeros de azucares"
patrón = r"\b\w+s\b" #"\b" delimita palabras, por ejemplo \bcat\b solo dara ocurrencia con cat, no cats
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan la secuencia de letras "ab".
texto = "abelardo es una persona con mucha sabiduria y calabazas"
patrón = r"(ab[a-z]+|[a-z]+ab[a-z]+|[a-z]+ab)" 
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan solo letras minúsculas.
texto = "Abelardo es Una persona con mucha sabiduria y calabazaS"
patrón = r"\b[a-z]+\b" #delimitamos palabras solo con minúsculas.
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan al menos una vocal.
texto = "abelardo de la espriella"
patrón = r"[aeiou](?=[a-z]+)[a-zA-Z0_9_]+|(?=[a-z]+[aeiou])[a-zA-Z0_9_]+" 
resultado = re.findall(patrón, texto)
print(resultado)

# manera mucho mas practica y eficiente:
texto = "abelardo de la espriella"
patrón = r"[aeiou][\w]+|[\w]+[aeiou]" 
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan exactamente tres letras
texto = "esta es una secuencia para probar palabras con tres letras"
patrón = r"\b[\w]{3}\b" # delimitamos 
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan solo números.
texto = "esta es una secuencia para probar palabras con 3 letras"
patrón = r"\b[\d]+\b"  
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan al menos una letra mayúscula.
texto = "Esta es una secuencia para probar Mayuscula"
patrón = r"[A-Z][\w]+|[\w]+[A-Z]"  
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan dígitos consecutivos.
texto = "Esta es una secuencia para probar 322"
patrón = r"\b[\d]{2,}+\b"  
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan una secuencia de tres vocales.
texto = "detector de treees vocaaales consecutiiivas iiimas maaa"
patrón = r"[\w]+[aeiou]{3}[\w]+|[aeiou]{3}[\w]+|[\w]+[aeiou]{3}"  
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan una repetición de la misma letra.
texto = "repeticion llana de la misma letra"
patrón = r"[a-z]+[\w]{2}[a-z]+"  
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan una secuencia de dos consonantes seguidas.
texto = "repeticion llana de la misma letra"
patrón = r"\w*[bcdfghjklmnpqrstvwxyz]{2}\w*" #"*" cero o muchas veces.
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan una secuencia de dos números separados por una coma.
texto = "1,2 3,4 5,,6 ,78, ,9 9,"
patrón = r"[0-9],[0-9]"  
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan una fecha en formato "dd/mm/aaaa".
texto = "Hoy es 80/06/2023 y mañana será 11/06/2023. La reunión está programada para el 12/06/2023."
patrón = r"\b\d{2}/\d{2}/\d{4}\b"
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan una dirección de correo electrónico válida.
texto = "recuerden enviar el correo kenifer@misena.edu.co y al alejandro0432@gmail.es"
patrón = r"\b\w+@\w+\.[\w.]+\b"# limitamos debido a que estamos buscando en una frase.
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan un número de teléfono válido.
texto = "+57 3137476895 3114439807"
patrón = r"(?:\+\d{1,3}\s)?\d{10}" #(?:) se usa para darme una condicion, pero sin darme la salida.
resultado = re.findall(patrón, texto)
print(resultado)    

# regex by chaatGPT.
texto = "Mi número de teléfono es +57 (123) 456-7890. Puedes llamarme al 555-123-4567."
patrón = r"\b(?:\+\d{1,3}\s)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
resultado = re.findall(patrón, texto)
print(resultado)

texto = "Mi número de teléfono es +57 (123) 456-7890. Puedes llamarme al 555-123-4567."
patrón = r"(?:\+\d{1,3}\s)?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}[.]?"
resultado = re.findall(patrón, texto)
print(resultado)
#(?:) aquí usamos un grupo debido a que "+57" es un valor con numero y signo, que juntos
# me conforman un valor opcional. en este caso entonces usamos esa expresion
# de otra manera me puede generar valores erroneos al poner por ejemplo \+\d{} por separado.

#Encuentra todas las palabras que contengan una secuencia de palabras separadas por un guion.
texto = "Mi número de teléfono es +57 (123) 456-7890. Puedes - llamarme al 555-123-4567."
patrón = r"\b\w+\s?-\s?\w+\b"
resultado = re.findall(patrón, texto)
print(resultado)

#Encuentra todas las palabras que contengan una cadena que se repita exactamente dos veces.
texto = "cadena de texto exactamente texto cadena"
patrón = r"\b(\w+)\b(?=.*?\b\1\b)"
resultado = re.findall(patrón, texto)
print(resultado)
# "\1" equivale al primer parentesis de la expresión, es decir (\w+) 



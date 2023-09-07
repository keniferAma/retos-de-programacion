"""/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cierran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */"""


string = "{ [ a * ( c + d ) ] - 5 }({[]})"

def regulador_de_expresiones(expresion):
    parametros = ""
    expresiones_erroneas = ""
    for elemento in expresion:
        if (elemento == "{" or elemento == "}" or 
            elemento == "(" or elemento == ")" or 
            elemento == "[" or elemento == "]"):

            parametros += parametros.join(elemento)                      
        
    while parametros:    
        if "()" in parametros:
            indice = parametros.index("()")
            primera_parte = parametros[:indice]
            segunda_parte = parametros[indice + 2:]
            parametros = primera_parte + segunda_parte

        elif "[]" in parametros:
            indice = parametros.index("[]")
            primera_parte = parametros[:indice]
            segunda_parte = parametros[indice + 2:]
            parametros = primera_parte + segunda_parte

        elif "{}" in parametros:
            indice = parametros.index("{}")
            primera_parte = parametros[:indice]
            segunda_parte = parametros[indice + 2:]
            parametros = primera_parte + segunda_parte
        
        else:
            expresiones_erroneas = parametros
            break
        
    if expresiones_erroneas:
        return f"Estas expresiones no están equilibradas: {expresiones_erroneas}"
    else:
        return "Expresiones bien equilibradas."
    


# print(regulador_de_expresiones(string))


### PROGRAMA HECHO POR LA INTELIGENCIA ARTIFICIAL:
# Por lo que logro observar, aquí se trata de obtener el primero valor de lo que queremos, es decir primero buscamos
# bien sea un paréntesis, un corchte o una llave y con el mismo bucle buscamos su contraparte; si está, damos 
# o arrojamos mejor un bool True, si no, False.
def esta_balanceada(expresion):
    pila = []
    for caracter in expresion:
        if caracter in ['(', '{', '[']: # Algo muy importante para tener en cuenta, creamos una lista con los
            # elementos que vamos a buscar en la expresión, de esta manera ahorramos espacio y queda más legible.
            pila.append(caracter)
        elif caracter in [')', '}', ']']:
            if not pila:
                return False
            ultimo = pila.pop() # Este pop lo que está haciendo es retornándome el último valor que se encuentra
            # en la lista, y al mismo tiempo nos lo está eliminando.
            # En la lista "pila" prácticamente solo alcanza a haber un elemento, y este es inmeditamente eliminado.
            if ultimo == '(' and caracter != ')':
                return False
            elif ultimo == '{' and caracter != '}':
                return False
            elif ultimo == '[' and caracter != ']':
                return False
    return not pila

print(esta_balanceada(string))
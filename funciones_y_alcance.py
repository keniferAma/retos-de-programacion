"""/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */"""


# funcion sin retorno #
def sumar(primer_numero, segundo_numero) -> int:
    """suma de dos numeros"""
    print(primer_numero + segundo_numero)

sumar(1, 5)


# funcion con retorno #
def restar(n1, n2) -> int:
    return n1 - n2

print(restar(2, 7))


# funcion dentro de otra funcion #

def multiplicacion_de_restas(n1) -> int:
    return n1 * restar(2, 4)

print(multiplicacion_de_restas(2))


def division(n1, n2):
    return n1 / n2

print(division(3, 90))


# variable local y global #

global_variable = 'This is the global variable'
print(global_variable)

def local_variable():
    my_local_variable = 'This is the local variable.'
    return my_local_variable

local_variable()
#print(my_local_variable) no es posible sin definir su variable interna con 'global'

def global_function():
    global my_global_variable  
    my_global_variable = 'This is the global variable inside of a local function'
    return my_global_variable

global_function()
print(my_global_variable) # nos imprime la variable, obviamente ejecutando previamente la funcion.




def retorno_de_numeros(texto_1, texto_2):
    resultado = 0
    for i in range(101):

        if i % 3 == 0 and i % 5 == 0:
            print(f'{texto_1} {texto_2}')
        elif i % 5 == 0:
            print(texto_2)
        elif i % 3 == 0:
            print(texto_1)
        else:
            print(i)
            resultado += 1

    return resultado    

print(retorno_de_numeros('string numero 1', 'string numero 2'))
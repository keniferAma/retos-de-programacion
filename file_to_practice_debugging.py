from typing import Iterable, Optional

def sacar_promedio(valores: Iterable[int]) -> Optional[float]:
    # if len(valores) < 5:
    #     return None
    
    return sum(valores) / len(valores) # AQUI PUSIMOS NUESTRO PUNTO DE INTERRUPCION
    # punto de interrupcion con expresion 'len(valores) > 4' en 'return'.
    # si es True (el programa corre normalmente tomando en nuestro caso 'lista_de_valores')
    # el pograma se detiene en el punto (sin ejecutarse) y nos muestra los valores.
    # Si por el contrario es False, el debug ignora dicho punto de interrupcion.

    # Caso contrario a asignar dicho punto de interrupcion sin Expresion.
    # ya que en este caso el programa se corta en el punto de interrupcion 
    # evitando que se ejecute la linea y, mostrando los estados hasta alli.

    # EXPRESIONES RECONOCEN TRUE OR FALSE, POR ESO NO SE CONFIGURAN CON CONDICIONALES (IF)

    # Punto de interrupcion con expresion 'isinstance(valores, set)' (set sin parentesis
    # porque de lo contrario estariamos creando un set vacio, lo cual nunca se cumpliria.)
    # en efecto nos da como false en 'otra_lista_de_valores'.


lista_de_valores = [1, 2, 3, 4, 5, 3, 44]

print(sacar_promedio(lista_de_valores))



otra_lista_de_valores = {1, 1, 1, 1}
print(sacar_promedio(otra_lista_de_valores))



# AGREGAR FUNCION A 'PUNTOS DE INTERRUPCION' #
# agregamos cualquier funcion (sin llamarla directamente con parentesis)
# y ejecutamos, entonces podremos ver la cantidad de veces que es llamada y el paso a paso.
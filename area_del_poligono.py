"""/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */"""


def poligonos(tipo: str, base: int, altura: int):
    match tipo.lower():
        case "cuadrado":
            return f"El resultado del area del cuadrado es: {base * altura}."
        case "rectangulo":
            return f"El resultado del area del rectángulo es: {base * altura}."
        case "triangulo":
            return f"El resultado del area del triángulo es: {(base * altura) / 2}."
        case other:
            return f"escribiste {other!r}, no se encuentra entre las opciones"
            """escribiste 'trangulo', no se encuentra entre las opciones"""
            # Este resultado nos lo imprimimos mediante repr, para que lo muestre tal cual fue escrito en el prompt.
        
        

    
    # if tipo.lower() == "cuadrado":
    #     return f"El resultado del area del cuadrado es: {base * altura}."
    
    # elif tipo.lower() == "rectangulo":
    #     return f"El resultado del area del rectángulo es: {base * altura}."
    
    # elif tipo.lower() == "triangulo":
    #     return f"El resultado del area del triángulo es: {(base * altura) / 2}."
    # else:
    #     return f"No escribiste el tipo de poligono de manera correcta."
    
    
    

print(poligonos("trangulo", 2, 2))
        

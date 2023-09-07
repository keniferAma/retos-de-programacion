"""/*
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
 */"""


def conversor(dias: int=0, horas: int=0, minutos: int=0, segundos: int=0):

    milisegundo = 1
    segundo = milisegundo * 1000
    minuto = segundo * 60
    hora = minuto * 60
    dia = hora * 24

    resultado_dias = dias * dia
    resultado_horas = horas * hora
    resultado_minutos = minutos * minuto
    resultado_segundos = segundos * segundo

    final_result = (
        resultado_dias +
        resultado_horas +
        resultado_minutos +
        resultado_segundos
    )
    return final_result


    
print(conversor(minutos=345))
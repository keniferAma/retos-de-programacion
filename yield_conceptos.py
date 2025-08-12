def generador_with_for():
    lista_a_iterar = [1, 2, 3, 4, 5]
    for n in lista_a_iterar:
        yield n


resultado = generador_with_for()

print(next(resultado))
print(resultado.__next__())



# La forma mas basica:

def generador_basico():
    yield "primer valor"
    yield "segundo valor"
    yield "tercer valor" # podemos ver que yield de por si es un iterador.


resultado_basico = generador_basico()

print(next(resultado_basico))

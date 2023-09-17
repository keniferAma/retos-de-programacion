# O(log n) recordar que su base siempre va a ser 2 (es la base de la computación)
# Esto anterior es la eficiencia de un algoritmo que esta clasificada en la tabla Big O como un algoritmo eficiente
# junto con O(1).


# O(1):
# complejidad constante, osea las más eficientes:
x = 1 + 2
y = 200*3
print(y)


# O(n)
# Complejidad lineal, es decir, entre mas aumenta n, mas
# tiempo va a tardar en ejecutarse. Muy común en bucles

numeros = "123456"
for n in numeros:
    print(n) # este print es complejidad O(1) pero lo limita n.
## PARA DETERMINAR LA EFICIENCIA DEL ALGORITMO NOS QUEDAREMOS CON LA MENOS EFICIENTE:
# En el anterior caso "numeros" es de complejidad O(1) al igual que el print
# Pero el bucle es de complejidad O(n), es decir esta es la complejidad constante del algoritmo.
# Debido a que dicha complejidad será la que lleva el ritmo del algoritmo.
 

# O(n2) 
# Complejidad cuadrática, es decir muy poco eficiente, este tipo de algoritmos es muy común con bucles
# anidados

for n in numeros: # O(n)
    for n in numeros: # O(n)
        print(n + n) # O(1)
# O(n) + O(n) = O(n2)


# O(log n)
# complejidad logaritmica de n, es cuando en un bucle por ejemplo la variable n es multiplicada o dividida.
# en el ejercicio anterior es O(n) debido a que n está imprimiendo de manera constante una lista.

n = 1 # O(1)
for f in n: # O(log n)
    print(f + 1) # O(1)
 

# O(n log n)
# este no es ni eficiente ni el peor, es muy común usarlo en condicionales if, else
# Es aquí donde podemos optimizar, muchas veces simplemente no necesitamos el else.

if x == 2:
    print("yes") # O(n)
else:
    print("no") # O(n log n)











def log(n):
    d = 0
    while n > 1:
        l = n / 2
        d = + 1
        print(d)
        return log(l)
    
    return d
    

print(log(256))
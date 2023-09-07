#fibonacci:

def fibonacci_by_me():
    result = 0
    suma_1 = 0
    suma_2 = 1
    for n in range(0, 20):
        result = suma_1 + suma_2
        if suma_1 <= suma_2:
            suma_1 = result
        else:
            suma_2 = result
        print(suma_1)
        
fibonacci_by_me()


#fibonacci by Brais:

def fibonachi_by_brais():
    prev = 0
    next = 1
    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonachi_by_brais()


    
        

    


            


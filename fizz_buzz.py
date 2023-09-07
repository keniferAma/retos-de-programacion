#fizz buzz 
#hacer un programa que me imprima los numeros del 1 al 50
#con salto de linea entre cada impresion
#multiplos de 3 sustituir por "fizz"
#multiplos de 5 sustituir por "buzz"
#multiplos de 3 y 5 al mismo tiempo por FizzBuzz

def fizzbuzz():
    for n in range(1, 51):
        if n % 3 == 0 and n % 5 == 0:# en este ejercicio observamos como juegó papel la posicion 
            # ya que si no estuviera al inicio, su resultado estaría limitado a las otra condicionales.
            espacio = " " * n + "FizzBuzz"
        elif n % 5 == 0:
            espacio = " " * n + "Buzz"
        elif n % 3 == 0:
            espacio = " " * n + "Fizz"
        else:
            espacio = (" " * n) + str(n)
        print(espacio)

fizzbuzz()
""" 
1
  2
   Fizz
    4
     Buzz       
      Fizz      
       7        
        8       
         Fizz   
          Buzz  
           11   
            Fizz
             13
              14
               FizzBuzz
                16
                 17
                  Fizz
                   19
                    Buzz
                     Fizz
                      22
                       23
                        Fizz
                         Buzz
                          26
                           Fizz
                            28
                             29
                              FizzBuzz
                               31
                                32
                                 Fizz
                                  34
                                   Buzz
                                    Fizz
                                     37
                                      38
                                       Fizz
                                        Buzz
                                         41
                                          Fizz
                                           43
                                            44
                                             FizzBuzz
                                              46
                                               47
                                                Fizz
                                                 49
                                                  Buzz"""
    

    
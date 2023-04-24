#Crea un bucle 'for' que imprime los números de 1 al 100. Para los múltiplos de 3 imprime la palabra "Fizz" en vez del número y para los múltiplos de 5 imprime "Buzz". 
# Para los números que son múltiplos de 3 y de 5, imprime “FizzBuzz”.


n = int(input("Cuántos números quiere imprimir?: "))

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    
    elif i % 5 == 0:
        print("Buzz")
        
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
        
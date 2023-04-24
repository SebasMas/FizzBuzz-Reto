#Crear un programa que invierta una cadena de texto.

#Establecemos una variable de tipo String que recibirá la cadena de texto, en este caso, una palabra.
cadena = input("Ingrese una palabra: ")

#Creamos un ciclo en el que imprima la palabra que ingresamos desde la última posición hasta la primera.
for i in cadena[-1::-1]:
    print(i)
    
#Otra opción más corta
print(cadena[-1::-1])
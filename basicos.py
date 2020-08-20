#Esto es un comentario
#print("Comentario")
print("Hola mundo!") 
print("Adios mundo!")

#Operadores aritmeticos
5+1
print(4+6)
print(5-2)
print(3*4)
print(20/4)
#Precedecia de operadores
print(5+8*(3+2))

#Tipos de datos
print(type(2))
print(type(8.62))
print(type("Texto"))
print(type('Texto'))
print(type("5"))

#Variables
mensaje = "Esto es un mensaje"
print(mensaje)
mensaje = "Mensaje modificado"
print(mensaje)
print(type(mensaje))
mensaje = 100
print(mensaje)
print(type(mensaje))

mis3aniamles = "Perico, gallo, chivo"
print(mis3aniamles)

tresAnimales = "Perico, gallo, chivo"
print(tresAnimales)


textoUno = "Mi texto "
textoDos = "Mi segundo texto"

print(textoUno + textoDos)

#str() int() float()
edad = 20
print("La edad del usuario es: " + str(edad))
print("El tipo de dato es: " + str(type(edad)))

import math

grados = 45.0
radianes = grados * math.pi / 180.0
seno = math.sin(radianes)
print("Seno de 45°: " + str(seno))

def saludar(nombre):
    print("Hola " + nombre)
    print("¿Como estas?")
    print("TE salido de lejos por eso del virus!")

def despedir():
    print("Ya me voy")
    print("Ya que pase todo esto nos abrazamos")

def concatenar(parte1, parte2):
    return parte1 + parte2

print("Esto no es parte de la funcion")
saludar("Damian")
despedir()

frase = concatenar("Hola ", "Adios ")
print(frase)

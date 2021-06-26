#!/usr/bin/env python
# coding: utf-8

# Ejercicio 1
# 
# Escribí un programa de python que imprima un diccionario cuyas claves sean los números de 1 a 15 y cuyos valores sean las potencias al cuadrado de estos números.

# In[54]:


diccionario = {}


# In[56]:


for numero in range(1,16):
    diccionario[numero] = numero**2
for clave, valor in diccionario.items():
    print(clave, valor)


# Ejercicio 2
# 
# Realizá un programa que imprima la suma de todos los valores de un diccionario de números.

# In[62]:


contador = 0
for valor in diccionario.keys():
    contador+= valor
print(contador)

print(sum(diccionario.values()))


# Ejercicio 3
# 
# Escribí un programa que obtenga, a partir de una lista de strings una lista con la longitud de esas strings e imprima la longitud de la lista de strings y los elementos de la lista de longitudes

# In[80]:


def extraerLongStrings (lista):
    listaNueva = []
    for elemento in lista:
        listaNueva.append(len(elemento))
    print ("hay", len(lista), "strings en la lista")
    print ("Sus longitudes son:")
    for long in listaNueva:
        print(long)


# Ejercicio 4
# 
# Realizá un programa que a partir de una lista mixta (que contiene distintos tipos de datos) imprima cuántos enteros tiene y además en el caso de los elementos que sean strings hay que crear una nueva lista con estos strings pero reemplazando al A por la U (tanto mayúscula como minúscula) y luego imprimir estos elementos.

# In[81]:


def contarEnteros(lista):
    contador = 0
    for elemento in lista:
        if type(elemento) is int:
            contador +=1
    print("hay", contador, "enteros")

def reemplazarAporU(lista):
    listaNueva = []
    for elemento in lista:
        if type(elemento)is


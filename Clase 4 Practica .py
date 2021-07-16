#!/usr/bin/env python
# coding: utf-8

# Manipulacion de Archivos

# Ejercicio 1
# 
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

# In[2]:


import re
import glob as gb
import os as os
text =open(r"C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\Verso1.txt")
with open (text,"r") as file:
    contador = 0
    for i in miarch:
            if i[0] !="L":
                contador +=1
print("Hay " + str(contador) + "lineas que no empiezan con la letra L")            


# Ejercicio 2
# 
# Escribí un programa que lea un archivo e imprima las primeras n líneas.

# In[4]:


import re

text = open(r"C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt")
def texto (archivo):
    contador = 0 
    with open(archivo, 'r') as file:
        for i in file:
            if i [0] != "T":
                contador +=1


# Ejercicio 3
# 
# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

# In[6]:


import re
path = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt'
with open (path,'r') as file:
    lista = file.readlines()
    print(lista)


# Ejercicio 4
# 
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado

# In[10]:


import re
path = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt'
with open (path, 'r') as file:
    texto = file.readlines()
    palabras = texto.split()
        print(len(palabras))


# Ejercicio 5
# 
# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

# In[1]:



import re
import shutil
route = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\txtmanip.txt'
newRoute = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\newtxtmanip.txt'
with open (route,"r") as txt:
    data = txt.read()
with open (newRoute,"w") as txt2:
    shutil.copyfile(route,newRoute)
with open (newRoute,"r+") as copy:
    copy.write(re.sub("s", "s\n",copy.read()))


# Ejercicio 6
# 
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

# In[ ]:


import re
import shutil
route = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\txtmanip.txt'
newRoute = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\txtsaltos.txt'
with open(route,"r") as txt:
    originalFile = txt.read()
with open(newRoute,"w") as newFile:
    shutil.copyfile(route,newRoute)
with open(newRoute,"r+") as alteredFile:
    for line in alteredFile:
        line = line.replace("\n", "")


# Ejercicio 7
# 
# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

# In[ ]:


import re
route = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\txtmanip.txt'
with open(route, 'r') as infile:
    txt = infile.read().split()
    max_len = len(max(txt, key=len))
    longest = [word for word in txt if len(word) == max_len]
    longest = re.split("[^a-zA-Z\d]+", str(longest))
    longest = ','.join([ i for i in longest if len(i) > 0 ])
    print(longest)
    print(len(longest))


# Ejercicio 8
# 
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

# In[ ]:


r1 = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\txtmanip.txt'
r2 = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\newtxtmanip.txt"
r1_r2 = r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\comb.txt'
with open(r1,"r") as txt1:
    t1 = txt1.read()
with open(r2,"r") as txt2:
    t2 = txt2.read()
t1 += "\n" + t2
with open(r1_r2,"w") as comb:
    comb.write(t1)


# Ejercicio 9
# 
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

# In[ ]:



import re
import string
frequency = {}
txt = open(r'C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\txtmanip.txt', "r")

data = txt.read()
w = data.split()
wcount = len(w)

match_pattern = re.findall(r'\b[a-z]{3,15}\b', data.lower())


for word in match_pattern:
  count = frequency.get(word,0)
  frequency[word] = count + 1
   
frequency_list = frequency.keys()
 
for words in frequency_list:
  fr = frequency[words]/wcount
  print(words, fr)


# Ejercicio 10
# 
# Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

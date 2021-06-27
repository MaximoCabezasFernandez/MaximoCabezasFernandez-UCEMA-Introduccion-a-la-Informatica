#!/usr/bin/env python
# coding: utf-8

# Ejercicio 1
# 
# Escribí un programa que sume, reste, multiplique y divida dos series de números de Pandas.
# 
# [3, 7, 12, 15, 21], [1, 4, 10, 14, 19]

# In[23]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss

serie1 = [3, 7, 12, 15, 21]
serie2 = [1, 4, 10, 14, 19]

df = pd.Series(serie1)
df2 = pd.Series(serie2)

ss = (df+df2)
print(ss)


# In[22]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss

serie1 = [3, 7, 12, 15, 21]
serie2 = [1, 4, 10, 14, 19]

df = pd.Series(serie1)
df2 = pd.Series(serie2)

rr = (df-df2)
print(rr)


# In[20]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss

serie1 = [3, 7, 12, 15, 21]
serie2 = [1, 4, 10, 14, 19]

df = pd.Series(serie1)
df2 = pd.Series(serie2)

mm = (df*df2)
print(mm)


# In[21]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss

serie1 = [3, 7, 12, 15, 21]
serie2 = [1, 4, 10, 14, 19]

df = pd.Series(serie1)
df2 = pd.Series(serie2)

dd = (df/df2)
print(dd)


# Ejercicio 2
# Realizá un programa que compare (si son mayores, menores o iguales) los elementos de dos series de números de Pandas.
# 
# Series de muestra:
# 
# [3, 7, 9, 14, 25], [1, 7, 10, 16, 19]

# In[26]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss

serie1 = [3, 7, 9, 14, 25]
serie2 = [1, 7, 10, 16, 19]

df = pd.Series(serie1)
df2 = pd.Series(serie2)

max = (df>df2)
print (max)


# In[30]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss

serie1 = [3, 7, 9, 14, 25]
serie2 = [1, 7, 10, 16, 19]

df = pd.Series(serie1)
df2 = pd.Series(serie2)

may = (df<df2)
print (may)


# In[31]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss

serie1 = [3, 7, 9, 14, 25]
serie2 = [1, 7, 10, 16, 19]

df = pd.Series(serie1)
df2 = pd.Series(serie2)

igu = (df==df2)
print (igu)


# Ejercicio 3
# Escribí un programa para convertir un diccionario a una serie de Pandas.
# 
# Diccionario de muestra:
# 
# dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

# In[37]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss

dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

sr = pd.Series(dict1)

print(sr)


# Ejercicio 4
# 
# Escribí un programa que dado un diccionario cuyos valores son listas de números, cree otro diccionario con las mismas claves, pero donde los valores sean una lista de números donde se potencia un número por el siguiente, tomándolos de a pares. Para ser más claros miremos este ejemplo donde si un diccionario es:
# 
# dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}
# 
# el diccionario resultante debería ser:
# 
# dict2 = {"a": [1, 25], "b": [16, 27]}
# 
# Esto se obtiene al hacer 1 al cubo (el primer par de la lista "a"), y 5 al cuadrado, por un lado; y 4 al cuadrado y 3 al cubo por el otro. Se considera que la cantidad de elementos en las listas siempre es par, por lo que no habría que hacer ninguna comprobación al respecto. Se puede usar el dict1 como diccionario de muestra, pero considerá que la lista puede ser más grande. Por último hay que convertir este último diccionario en un DataFrame de Pandas.

# In[62]:


import pandas as pd

dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}

dict2 = {}

for clave in dict1.keys():
    dict2[clave]=[]
    for numero in dict1[clave]:
        if dict1[clave].index(numero)%2==0:
            dict2[clave].append(numero**dict1[clave][(dict1[clave].index(numero))+1])
print(dict2)


# Ejercicio 5

# Muestra:
# 
# datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
# 
# labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# In[4]:


import pandas as pd

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(datos_ejemplo, index = labels)

print(df)


# Ejercicio 6
# Escribí un programa que muestre un resumen de la información básica de un DataFrame y sus datos.
# 
# Muestra:
# 
# datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
# 
# labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# 

# In[1]:


datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

import pandas as pd

df = pd.DataFrame(datos_ejemplo)
print(df)


# In[54]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


df = pd.DataFrame(datos_ejemplo)
df2 = pd.DataFrame(labels)
aa = df.info
ss = df2.info


# Ejercicio 7
# Escribí un programa que obtenga las 3 primeras filas de un DataFrame dado.
# 
# Muestra:
# 
# datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
# 
# labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# In[17]:


import pandas as pd
df1 = pd.DataFrame({"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]})

print(df1)
df.loc[df.index[0:3]]


# Ejercicio 8
# 
# Realizá un programa que seleccione e impirma las columnas "nombre" y "puntaje" del DataFrama anterior.

# In[27]:


import pandas as pd
df1 = pd.DataFrame({"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]})
dfNyP = df1[df1.columns[0:2]]
print(dfNyP)


# Ejercicio 9
# 
# Escribí un programa que dado el DataFrame anterior imprima los nombres en mayúscula y la longitud de los mismos en una nueva tabla

# In[8]:


import pandas as pd
df1 = pd.DataFrame({"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]})
dfNyP = df1[df1.columns[0:2]]
df1NyP = dfNyP["nombre"].str.upper()
df1NyP.str.len()


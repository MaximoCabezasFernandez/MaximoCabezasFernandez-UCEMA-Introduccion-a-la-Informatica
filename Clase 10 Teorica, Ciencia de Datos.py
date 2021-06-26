#!/usr/bin/env python
# coding: utf-8

# Introduccion a la Ciencia de Datos con Python
# 
# Se necesitan 3 bibliotecas, que son Pandas, Seaborn (visualizacion de datos) y Scipy (estadisticas)

# In[1]:


import pandas as pd
import seaborn as sns
import scipy.stats as ss


# Trabajamos con datasets, estas son bases de datos

# Un osito cariñosito
# 
# Vamos a utilizar Pandas, nos permite trabajar con archivos definidos, CSV(Coma Separated Values), un excel etc. Pandas es lo mas parecido a excel.
# 
# Para pensar, una biblioteca nos permite realizar funciones que la biblioteca de python no tiene. Un archivo que incluye metodos. 
# 
# Pandas trabaja con datos estructurados, de columnas. 
# De lo conceptual, un archivo tabulado, esta separado mediante la funcion de TAB o \t.
# 

# In[2]:


import requests


# In[3]:


r = requests.get("https://datasets.datos.mincyt.gob.ar/dataset/06ae9728-c376-47bd-9c41-fbdca68707c6/resource/fdcfe792-a17f-4e7d-9bae-ba8a47d8ba3e/download/personas_2011.json")


# In[4]:


r.json()


# Tambien se puede obtener usando .json()

# Pandas maneja 2 estructura de datos, Series y DataFrames.
# 
# Series (1-dimensional) Las series pueden contener cualqueir tipo de datos, enteros, cadenas, números de punto flotante, etc.). Y se pueden crear del siguiente modo:

# In[6]:


import pandas as pd
una_serie = pd.Series(['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], dtype='string')
print(una_serie)


# Data Frames (2-Dimensional)
# 
# Un DF es una estructura tipo tabular bidimensional de datos tabulares, potencialmente heterogeneos, con ejes etiquetados (filas y columnas) es muy similar a un diccionario osea, un dict. 

# In[7]:


paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])

print(paises_latam)


# Primero que nada renombramos la variable y utilizamos la biblioteca de pd.DataFrame
# 
# Luego, dentro del parentesis renombramos la columna, y dentro de la columna le asignamos valores. Cerramos la columna y si queremos abrir otra columna realizamos el metodo anterior.  

#     Una forma muy usual de generar DF es mediante la lectura de archivos estructurados.
# 
#     El caracter de separacion de archivos con columnas: read_csv es una coma
# 
#     df = pd.read_csv(path del archivo, sep=";") el Sep cumple la funcion de separar el parametro que inculyamos entre las comillas. 
# 
#     El caracter de separación de columnas por defecto del método read_fwf es una tab ('\t').
# 

#     Trabajando con DF
# 
#     df.head() - Para la previsualizacion de los datos. 
#     df.info() - Averiguar la informacion grla de tu tabla.
#     df.describe() - Informacion nos ayuda a saber los nombres de las columnas de nuestra tabla, o el tipo de datos que contene.
#     df['nombre de la columna'] - Para acceder a los datos de cada columna
#     df.loc[fila, columna] - Datos de una celda en particular.
#     df['columna'].tolist() - Acceder a los datos de una columna del DF como una lista.
#     df['columna'] *+> numero - Podemos operar con las columnas con los mismos operadores relacional y matematicos
# 
#     df[df['columna'] > 35] - Los operadores tambien nos sirven para filtrar DF
#     df3 = pd.merge(df, df_cat, on='categoria_conicet_id') -  Poder realizar analisis de datos filtrando por categoria, el metodo merge funciona para unir columnas
#     df3 = pd.concat([df, df_cat,]) 

# Desafio 4

# In[12]:


path = r"C:\Users\PC\Downloads\personas_2011.csv"
import pandas as pd
df = pd.read_csv(path, sep=";")
df['seniority_level'].value_counts()


# In[14]:


df["seniority_level"].count()


# In[15]:


df.groupby("seniority_level").count()


# In[16]:


df.groupby("seniority_level")[["persona_id"]].count()


# Desafio 5

# In[17]:


anio2011=df[df["anio"]==2011]
anio2011[anio2011["edad"]>30]


# Metodo de los Data Frames

#     Lectura/carga de datos
# 
#     pd.read_csv()
#     pd.read_table()
#     pd.read_excel()
#     pd.read_sql()
#     pd.read_json()
#     pd.to_csv()
#     pd.DataFrame()
#     pd.concat()
#     pd.Series()
#     pd.DataFrame.from_dict()

#     Limpieza de los datos
# 
#     pd.head()
#     pd.fillna()
#     pd.dropna()
#     pd.sort_values()
#     pd.groupby()
#     pd.apply()
#     pd.append()
#     pd.rename()
#     pd.set_index()
#     pd.tail()

#     Estdistica de los datos
# 
#     pd.describe()
#     df.sample()
#     pd.mean()
#     pd.median()
#     pd.std()
#     pd.min()
#     pd.max()
#     pd.count()
#     pd.corr()
#     pd.hist()

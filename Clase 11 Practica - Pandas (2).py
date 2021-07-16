#!/usr/bin/env python
# coding: utf-8

# Pandas

# pandas.read_csv
# 
# sep: indica como separar los elementos. Por defecto es la com ","
# 
# header: Si no le pasa una lista de encabezados toma la primera fila como la misma.
#             Se puede seleccionar cualquier fila como encabezado. Si directamente no se quiere usar encabezado y ningun dato, se utiliza None. 
# 
# dtype: Indica el tipo de datos del DF. Por defecto detecta el tipo de datos por columna
# 
# skiprows: ignora un numero de filas por defecto es 0
# 
# nrows: cantidad de lineas que se leen del archivo. Sirve cuando el archivo es muy grande
# 
# df.head: muestra un numero dado de la parte inicial del df por defecto su valor es 5
# df.tail: de igual manera muestra un numero dado del final del df por defecto su valor es 5
# df.max(): nos dice el valor maximo por columna
# df.min(): nos dice el valor minimo por columna
# df.count() devuelve la cantidad de datos no nulos de cada columna
# 
# Imprimir los valor de todas las columnas, cuyas filas sean mayores a 0 en la columna A:
# (df.loc[df["A"]>0])
#         Esta parte actua como un *
#         
#         
# Uniones
# 
# pandas.concat()
# 
# Se pueden concatenar objetos de manera de unirlos generando nuevas columnas y/o nuevas filas.
#       Se puede alterar de la siguiente manera, join= "inner", podemos querer la interseccion de los DF, por defecto es outer.
#       Se pueden alterar los cuadros usando, axis=1, por defecto es axis=01
#                
#       
# pandas.append()
# 
# Es un metodo anterior a concat() el cual no midifica el df
# 
# Al unir dos DF podemos ignorar los indices en las filas de modo que sean consecutivas, y que no mantengan la identidad de los df originales
#     ignore_index=True
# 
# to_dict(), to_list()
# 
# DF pueden ser guardados como diccionarios. 
# Las serie se pueden guardad tanto en listas como diccionarios
# 
# Si la serie no tiene indices, las claves del diccionario se completan automaticamente.

# Ejercicio 1
# 
# Escribí un programa que dado un diccionario cuyos valores sean listas de números cree un DataFrame y luego seleccione e imprima las filas del DataFrame basado en un valor de una columna.
# 
# Diccionario de muestra: {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}, y el valor es 4 en la columna 1.

# In[2]:


import pandas as pd 

diccionarioMuestra = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df = pd.DataFrame(diccionarioMuestra)

print(df[1])


# Ejercicio 2
# 
# Escribí un programa que guarde en una lista una columna de un DataFrame.

# In[3]:


import pandas as pd
paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])

df = pd.DataFrame(paises_latam, columns= ['Pais', 'Lengua oficial primaria'])
lista_paises = df.values.tolist()

print(lista_paises)


# Ejercicio 3
# 
# Realizá un programa que agregue datos a un DataFrame vacío.

# In[4]:


import pandas as pd

emptydf = pd.DataFrame()

def Addcoll(header , dt):
  emptydf[header] = dt

def Addrow(index , dt):
  emptydf.loc[index] = dt

Addcoll("name", ["Maximo","Maite","German","Manuela","Quentin"])
Addcoll("surname", ["Cabezas","Capalbo","Usinger","Blanco","Tarantino"])


# Ejercicio 4

# In[5]:



import pandas as pd

dic = {"Name" : ["Maximo","Maite","German","Manuela","Quentin"],
       "Surname" : ["Cabezas","Capalbo","Usinger","Blanco","Tarantino"],
       }

df = pd.DataFrame(dic)
newdf = pd.DataFrame()

def DeleteRows(n):
    global newdf
    newdf = df.tail(len(df)-n)
    print(newdf)


# Ejercicio 5

# In[6]:


import pandas as pd

def CheckColl(coll,df):
  try:
    print(df[coll])
  except:
    print("No hay una columna definida" + coll + "en el DataFrame")


# Ejercicio 6

# In[7]:


alumnos6a_dict={"Nombre":["Juana","Pedro","Carlos"],"Nota Matemática":[10,8.5,6],"Nota Lengua":[9,7,8],"Nota Ed. Física":[7,7,8]}
alumnos6b_dict={"Nombre":["Luis","Martina","Camila"],"Nota Matemática":[9,7,5.5],"Nota Lengua":[10,8,7],"Nota Baile":[9,8,7]}

alumnos6a_df=pd.DataFrame(alumnos6a_dict)
alumnos6b_df=pd.DataFrame(alumnos6b_dict)

alumnos_sexto_eje=pd.concat([alumnos6a_df,alumnos6b_df],ignore_index=True,axis=0)

alumnos_sexto_eje


# Ejercicio 7

# In[8]:


alumnos6a_dict={"Nombre":["Juana","Pedro","Carlos"],"Nota Matemática":[10,8.5,6],"Nota Lengua":[9,7,8],"Nota Ed. Física":[7,7,8]}
alumnos6a_df=pd.DataFrame(alumnos6a_dict)

alumnos6a_df

nota_ingles6a=[7,6,8]
alumnos6a_df["Nota Inglés"]=nota_ingles6a

alumnos6a_df


# Ejercicio 8

# In[9]:


alumnos6a_dict={"Nombre":["Juana","Pedro","Carlos"],"Nota Matemática":[10,8.5,6],"Nota Lengua":[9,7,8],"Nota Ed. Física":[7,7,8]}
alumnos6b_dict={"Nombre":["Luis","Martina","Camila"],"Nota Matemática":[9,7,5.5],"Nota Lengua":[10,8,7],"Nota Baile":[9,8,7]}

alumnos6a_df=pd.DataFrame(alumnos6a_dict)
alumnos6b_df=pd.DataFrame(alumnos6b_dict)

alumnos_sexto_eje=pd.concat([alumnos6a_df,alumnos6b_df],ignore_index=True,axis=0,join="inner")

alumnos_sexto_eje


# In[ ]:





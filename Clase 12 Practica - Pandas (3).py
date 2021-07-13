#!/usr/bin/env python
# coding: utf-8

#     El uso de la funcion de Merge
#         Fusiona 2 DF de la manera que le indiquemos
#     pd.merge()
#         how: indica la manera de uniion de los df, por defecto esta puesto como inner
#         on: indica en base a que columna se van a unir los DF, esta columna tiene que ser comun entre los 2
#         left_on: nombre de la columna de los datos de la izquierda el cual va usar para unir losDF
#         right_on: igual al anterior, pero con una columna de los datos de la derecha.
#         

# Creá un nuevo DataFrame a partir del DataFrame Personas, el cual solo tenga las columnas "persona_id", "anio" y "categoria_conicet_id" (guardalo en una variable llamada pers)

# In[33]:


import pandas as pd
conicet = pd.read_csv(r"C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\Bases de Datos\ref_categoria_conicet.csv", sep=";")
personas = pd.read_csv(r"C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\Bases de Datos\personas_2011.csv", sep=";")
pers = pd.concat([personas["persona_id"], personas["anio"], personas["categoria_conicet_id"]], axis = 1)
print(pd.merge(pers, conicet,how="right", on = "categoria_conicet_id"))
print(pd.merge(pers, conicet, how="left", on = "categoria_conicet_id"))


# In[22]:


pd.merge(pers, conicet,how="left", on = "categoria_conicet_id")


# In[18]:


pd.merge(pers, conicet,how="outer", on = "categoria_conicet_id")


# In[23]:


pd.merge(pers, conicet, left_on="persona_id", right_on = "categoria_conicet_id")


# Ejemplo de como seria el left_on y right_on
# 
# pd.merge(pers, conicet, left_on="persona_id", right_on = "categoria_conicet_id")

#     pd.df.set_index
#     
#     Mediante este metodo se puede definir el indice (nombre de las filas) de manera explicita
#         

# In[32]:


df = pd.DataFrame({'mes': [1, 4, 7, 10], 'anio': [2012, 2014, 2013, 2014], 'venta': [55, 40, 84, 31]})
print(df)
print(df.set_index('anio'))
print(df.set_index(['anio', 'mes']))


#     pd.df.sort_values
#         Ordena los valores de un DF. Se puede hacer tanto por columnas como por filas y eligiendo donde deber ir los nan
#         
#         axis: por defecto es 0. Con esto elegimos si se ordenan las columnas o las filas.
# 
#     ascending: por defecto es True, por lo que se ordena de menor a mayor. Si es False se invierte el orden.
# 
#     na_position: por defecto es "last", por lo que todos los valores NaN.
#     se ordenan al final, pero se puede configurar como "first" para que aparezcan primero.
#     

#     pd.df.to_csv
#     
#     Con este metodo podemos guardar un DF en un archivo CSV separado por comas
#     
#     path_or_buf: por defecto es None, por lo que si no le asociamos una ruta donde debe ser guardada nos va a devolver un string.
#     
#     sep: por defecto el separador es una coma
#     
#     na_rep: representacion de los valores NaN, que por defecto es un string vacio pero tambien puede ser configurado.
#     
#     header: por defecto es True, guarda el archivo con los nombres de las columnas
#     
#     index: idem a header, cuando los nombres de los indices son generados automaticamente, es mejor que este parametro tome el valor false

# In[1]:



import pandas as pd

personas = pd.read_csv("https://datasets.datos.mincyt.gob.ar/dataset/06ae9728-c376-47bd-9c41-fbdca68707c6/resource/11dca5bb-9a5f-4da5-b040-28957126be18/download/personas_2011.csv",sep=";")
ref_categoria_conicet = pd.read_csv("https://datasets.datos.mincyt.gob.ar/dataset/06ae9728-c376-47bd-9c41-fbdca68707c6/resource/c72c9f88-d9ef-4349-bb20-5c9a1aca5d67/download/ref_categoria_conicet.csv",sep=";")

personas_10mayores_provisorio=personas.sort_values(by=["edad"],ascending=False).head(10)
personas_10mayores = pd.concat([personas_10mayores_provisorio["persona_id"],personas_10mayores_provisorio["anio"],personas_10mayores_provisorio["edad"],personas_10mayores_provisorio["producciones_ult_4_anios"],personas_10mayores_provisorio["categoria_conicet_id"]],axis=1)
personas_10mayores_casi_final = pd.merge(personas_10mayores,ref_categoria_conicet)
personas_10mayores_final = pd.concat([personas_10mayores_casi_final["persona_id"],personas_10mayores_casi_final["categoria_conicet_descripcion"]],axis=1)


# In[ ]:





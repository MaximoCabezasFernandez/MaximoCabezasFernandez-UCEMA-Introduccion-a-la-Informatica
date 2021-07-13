#!/usr/bin/env python
# coding: utf-8

#                             -Estadistica-

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib as mp

datos = pd.read_csv(r"C:\Users\PC\Desktop\Datos.csv")
print(datos)


# In[2]:


datos.head()


# In[3]:


datos.info()


# In[4]:


datosFiltrados = datos.dropna()


# In[5]:


datosFiltrados.describe()


# In[6]:


datosFiltrados2 = datosFiltrados[datosFiltrados['Altura']<2.3]


# In[7]:


print(datosFiltrados2)


# In[8]:


datosFiltrados2.describe()


# In[9]:


datosFiltrados2.plot.scatter('Nombres', 'Sueldo')


# In[10]:


datosFiltrados3 = datosFiltrados2[datosFiltrados2['Sueldo']<200000]


# In[11]:


datosFiltrados3.describe()


# In[12]:


datosFiltrados3.plot.scatter('Nombres', 'Sueldo')


# In[13]:


datosFiltrados3.plot.scatter('Nombres', 'Altura')


# In[14]:


datosFiltrados3['Sueldo'].mode()


# In[15]:


datosFiltrados3['Altura'].mode()


# In[16]:


datosFiltrados3['Altura'].plot.density()


# In[17]:


import seaborn as sns
p = sns.pairplot(datosFiltrados3)


# In[ ]:





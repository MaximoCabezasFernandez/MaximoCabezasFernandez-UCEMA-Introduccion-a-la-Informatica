#!/usr/bin/env python
# coding: utf-8

#     Paso 0

# In[1]:


import pandas as pd  
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import seaborn as sns 
import numpy as np  
from sklearn import datasets  
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances
from scipy.cluster.hierarchy import dendrogram, cophenet, linkage
from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist
import networkx as nx 


#     Paso 1

# In[2]:


stock_data = pd.read_csv(r"C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\Bases de Datos\dataset_clustering_teorico.csv")
stock_data.head()


#      Paso 2

# In[3]:


stock_data.info()


# In[4]:


stock_data.describe()


# In[5]:


stock_data.dropna()


# In[6]:


descripcion_por_empresa=pd.DataFrame()
descripcion_por_empresa["Empresas"]=stock_data["Unnamed: 0"]
descripcion_por_empresa["Media"]=stock_data.mean(axis=1)
descripcion_por_empresa["Mediana"]=stock_data.median(axis=1)
descripcion_por_empresa["Mínimo"]=stock_data.min(axis=1)
descripcion_por_empresa["Máximo"]=stock_data.max(axis=1)
descripcion_por_empresa


# In[7]:


g = sns.pairplot(descripcion_por_empresa)


# In[8]:


g_medias = sns.histplot(data = descripcion_por_empresa, x = "Media", binwidth=0.25, kde = True)


# In[9]:


g_medianas = sns.histplot(data = descripcion_por_empresa, x = "Mediana", binwidth=0.25, kde = True)


# In[10]:


g_min = sns.histplot(data = descripcion_por_empresa, x = "Mínimo", binwidth=0.25, kde = True)


# In[11]:


dxe_solo_float=pd.DataFrame()
dxe_solo_float["Media"]=descripcion_por_empresa["Media"]
dxe_solo_float["Mediana"]=descripcion_por_empresa["Mediana"]
dxe_solo_float["Mínimo"]=descripcion_por_empresa["Mínimo"]
dxe_solo_float["Máximo"]=descripcion_por_empresa["Máximo"]
dxe_solo_float


# In[12]:


scaler=StandardScaler()
dxe_escaleado=scaler.fit_transform(dxe_solo_float)


# In[13]:


kmeans2 = KMeans(n_clusters = 2, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans2.fit(dxe_escaleado)


# In[14]:


colores2 = ["red", "green"]
g_grupos2 = sns.scatterplot(x = dxe_escaleado[:,2], y = dxe_escaleado[:,3], hue = kmeans2.labels_, palette = colores2, alpha = 0.5)
g_centroides2 = sns.scatterplot(x = kmeans2.cluster_centers_[:,2], y = kmeans2.cluster_centers_[:,3], zorder = 10, palette = colores2, hue = [0, 1], legend = False, marker=6, s=200)


# In[15]:


kmeans3 = KMeans(n_clusters = 3, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans3.fit(dxe_escaleado)


# In[16]:


colores3 = ["red", "green", "blue"]
g_grupos3 = sns.scatterplot(x = dxe_escaleado[:,2], y = dxe_escaleado[:,3], hue = kmeans3.labels_, palette = colores3, alpha = 0.5)
g_centroides3 = sns.scatterplot(x = kmeans3.cluster_centers_[:,2], y = kmeans3.cluster_centers_[:,3], zorder = 10, palette = colores3, hue = [0, 1, 2], legend = False, marker=6, s=200)


# In[17]:


kmeans4 = KMeans(n_clusters = 4, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans4.fit(dxe_escaleado)


# In[18]:


colores4 = ["red", "green", "blue", "yellow"]
g_grupos4 = sns.scatterplot(x = dxe_escaleado[:,2], y = dxe_escaleado[:,3], hue = kmeans4.labels_, palette = colores4, alpha = 0.5)
g_centroides4 = sns.scatterplot(x = kmeans4.cluster_centers_[:,2], y = kmeans4.cluster_centers_[:,3], zorder = 10, palette = colores4, hue = [0, 1, 2, 3], legend = False, marker=6, s=200)


# In[19]:


kmeans5= KMeans(n_clusters =5, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans5.fit(dxe_escaleado)


# In[20]:


colores5 = ["red", "green", "blue", "yellow", "violet"]
g_grupos5 = sns.scatterplot(x = dxe_escaleado[:,2], y = dxe_escaleado[:,3], hue = kmeans5.labels_, palette = colores5, alpha = 0.5)
g_centroides5 = sns.scatterplot(x = kmeans5.cluster_centers_[:,2], y = kmeans5.cluster_centers_[:,3], zorder = 10, palette = colores5, hue = [0, 1, 2, 3, 4], legend = False, marker=6, s=200)


# In[21]:


inertias_dict={}
inertias_dict["K"]=[]
inertias_dict["Inertia"]=[]
for i in range(15):
  k = i + 1
  kmeans_ = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457)
  kmeans_.fit(dxe_escaleado)
  inertias_dict["K"].append(k)
  inertias_dict["Inertia"].append(kmeans_.inertia_)
print(inertias_dict)


# In[22]:


inertias_df=pd.DataFrame(inertias_dict)
inertias_df


# In[23]:


sns.pointplot(data=inertias_df,x="K",y="Inertia")


# In[24]:


#PASO 2
stock_data_solo_float=stock_data.drop(["Unnamed: 0"],axis=1)
scaler=StandardScaler()
stock_data_normalizado=scaler.fit_transform(stock_data_solo_float)


# In[25]:


#PASO 3
kmeans14= KMeans(n_clusters = 14, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans14.fit(stock_data_normalizado)


# In[26]:


import matplotlib.colors as mcolors
colores14 = ["darkgray","lightcoral","firebrick","orangered","peru","lightgreen","yellow","bisque","green","turquoise","darkslategray","purple","deeppink","cadetblue"]
g_grupos14 = sns.scatterplot(x = stock_data_normalizado[:,2], y = stock_data_normalizado[:,3], hue = kmeans14.labels_, palette = colores14, alpha = 0.5)
g_centroides14 = sns.scatterplot(x = kmeans14.cluster_centers_[:,2], y = kmeans14.cluster_centers_[:,3], zorder = 10, palette = colores14, hue = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], legend = False, marker=6, s=200)


# In[27]:


kmeans8= KMeans(n_clusters = 8, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans8.fit(stock_data_normalizado)


# In[28]:


colores8 = ["darkgray","lightcoral","firebrick","orangered","peru","lightgreen","yellow","bisque"]
g_grupos8 = sns.scatterplot(x = stock_data_normalizado[:,2], y = stock_data_normalizado[:,3], hue = kmeans8.labels_, palette = colores8, alpha = 0.5)
g_centroides8 = sns.scatterplot(x = kmeans8.cluster_centers_[:,2], y = kmeans8.cluster_centers_[:,3], zorder = 10, palette = colores8, hue = [0, 1, 2, 3, 4, 5, 6, 7], legend = False, marker=6, s=200)


# In[29]:


kmeans6= KMeans(n_clusters = 6, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans6.fit(stock_data_normalizado)


# In[30]:


colores6 = ["darkgray","lightcoral","firebrick","orangered","peru","lightgreen"]
g_grupos6 = sns.scatterplot(x = stock_data_normalizado[:,2], y = stock_data_normalizado[:,3], hue = kmeans6.labels_, palette = colores6, alpha = 0.5)
g_centroides6 = sns.scatterplot(x = kmeans6.cluster_centers_[:,2], y = kmeans6.cluster_centers_[:,3], zorder = 10, palette = colores6, hue = [0, 1, 2, 3, 4, 5], legend = False, marker=6, s=200)


# In[ ]:





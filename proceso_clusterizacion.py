#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Librería para la normalización de datos 
from sklearn.preprocessing import StandardScaler
# Librería para aplicación de Componentes Princiales
from sklearn.decomposition import PCA
# Librearías  para clusterización y métricas de evaluación
from sklearn.cluster import KMeans,AgglomerativeClustering 
import pandas as pd


# In[5]:


dataset_consolidado_canton=pd.read_csv('C:/Users/Byron/Documents/curso_power_bi_sri/data_consolidada_canton.csv')


# In[2]:


dataset_consolidado_canton
campos_numericos=['Suma de Total Compras','Suma de Total Ventas','Suma de Ventas Netas 0%','Suma de Ventas Netas 12%',
                  'Suma de Importaciones','Suma de Exportaciones',
                  'Suma de Compras Rise','Suma de Compras netas 12%','Suma de Compras netas 0%']

campos_numericos_100K=['Suma de Total Compras','Suma de Total Ventas','Suma de Ventas Netas 0%','Suma de Ventas Netas 12%',
                  'Suma de Importaciones','Suma de Exportaciones',
                  'Suma de Compras Rise','Suma de Compras netas 12%','Suma de Compras netas 0%']


# In[3]:


# Estandarización de datos numéricos de acuerdo al número de habitantes (x cada 10000 habitantes )
contador_campos_numericos=0
for campo in campos_numericos:    
    dataset_consolidado_canton[campo]=dataset_consolidado_canton[campos_numericos[contador_campos_numericos]]*10000/dataset_consolidado_canton['Suma de Habitantes']
    contador_campos_numericos=contador_campos_numericos+1


# In[12]:


#Normalización de datos
# Obtención de dataset únicamente con datos numéricos para aplicar procesos de normalización, PCA y clusterización
dataset_consolidado_canton_Num=dataset_consolidado_canton.loc[:,campos_numericos ]
scaler=StandardScaler()
dataset_normalizado=scaler.fit_transform(dataset_consolidado_canton_Num)


# In[14]:


# Cálculo de PCA utilizado 2 componentes 
pca=PCA(n_components=2)
pca.fit(dataset_normalizado)
pca.transform(dataset_normalizado)
scores_pca=pca.transform(dataset_normalizado)


# In[24]:


# CLUSTERIZACION KMEANS
metricas_evaluacion_kmeans=list()
data_for_scatter=scores_pca
kmeans = KMeans(n_clusters = 3).fit(data_for_scatter)

#Consolidado cluster
dataset_consolidado_canton['cluster']=kmeans.labels_


# In[25]:


dataset_consolidado_canton.to_excel("C:/Users/Byron/Documents/curso_power_bi_sri/consolidado_cluster.xlsx")  


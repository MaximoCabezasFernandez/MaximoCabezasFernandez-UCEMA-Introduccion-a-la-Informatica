#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Ave:
    def esta_feliz(self):
        return self.energia >500 


# In[6]:


class Golondrina(Ave):
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
        self.energia += 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms
  
    def esta_debil(self):
        if self.energia <=10:
            print("Esta muy debil")
        if self.energia <0:
            print("Lamentamos el fallecimiento de" + "self")
  
    def esta_feliz(self):
        if self.energia >500:
            print("Nuestros animales estan muy felices")


# In[7]:


class Dragon(Ave):     
    def __init__(self, cantidad_dientes, energia):
        self.energia = energia
        self.cantidad_dientes = cantidad_dientes

    def escupir_fuego(self):
        self.energia -= 2 * self.cantidad_dientes

    def comer_peces(self, unidades):
        self.energia += 100 * unidades

    def volar_en_circulos(self):
        self.energia -= 1

    def volar(self, kms):
        self.energia -= 10 + kms/10
  
    def esta_debil(self):
        if self.energia <=10:
            print("Esta muy debil")
        if self.energia <0:
            print("Lamentamos el fallecimiento de" + "self")
  
    def esta_feliz(self):
        if self.energia >500:
            print("Nuestros animales estan muy felices")


# In[10]:


class EntrenadorDeDragones():
    def __init__(self,vacantes):
        self.vacantes = vacantes
        self.dragones_aceptados = []

    def aceptarDragones(self, dragon):
        if self.vacantes > 0:
            self.dragones_aceptados.append(dragon)
            self.vacantes -= 1 
  
    def entrenamiento (self):
        for dragon in self.dragones_aceptados:
            for _ in range (0, 20):
                dragon.volar_en_circulos()


# In[11]:


pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10,1000)


# In[ ]:





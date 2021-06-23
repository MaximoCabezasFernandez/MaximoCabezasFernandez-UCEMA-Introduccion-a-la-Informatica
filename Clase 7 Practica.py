#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Perro:
    def __init__(self):
        self.alimentos = 0
        self.caricias = 0
        
    def energia(self):
        return self.alimento + (self.caricias *10)
    def comer(self, gramos):
        self.alimento += gramos
    def alimento(self):
        print(self.alimento)
    def acariciar(self):
        self.caricias += 1
    def estaDebil(self):
        return self._caricias < 2
    def pasear(self, km):
        self.alimento -= km / 4


# In[2]:


class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
        print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4


# ¿Cuales son sus estados?
# 
# Los estados en ambas clases es alimento y caricias

# ¿Son polimorficas?
# 
# Comparten parte de la interfaz pero con distinta finalidad

# ¿Comparten su interfaz?
# 
# Podemos ver que comparten ciertas partes pero no por completo.
#     La interfaz que comparten es energia, comer, acariciar y estaDebil.

# ¿Cuales son sus interfaces?
# 
# Son los conjuntos de metodos, por ende serian
#     Las del gato, energia, comer, caricias, acariciar, estaDebil
#     Las del perro, energia, comer, alimento, acariciar, estaDebil, pasear.
#         

# Ejercicio 2
# 
# Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este estado se alcanza cuando la energía se encuentra entre 150 y 300.

# In[1]:


class Golondrina(Ave): # Golondrina hereda de Ave
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
        self.energia = self.energia + 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms

    def esta_debil(self):
        return self.energia <= 10
    
    def saciar(self):
        self.comer_alpiste(100)
    
    def estaEnEquilibrio (self):
        return self.energia > 150 and self.energia <300
    


# Ejercicio 3
# Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o Jeuna golondrina. Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos. Se propone:
# 
# implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().
# 
# comprobar el código que se escribió con esta secuencia:
# 
# definir un ornitólogo, dos golondrinas y dos gorriones,
# inicializar las aves con valores conocidos,
# decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
# decirle al ornitólogo que realice su rutina sobre aves,
# verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.

# In[ ]:



class Ornitologo:
    def __init__(self):
        self.aves_en_estudio=[]

    def estudiarAve(self, ave):
        self.aves_en_estudio.append(ave)
  
  def avesEnEstudio(self):
    self.aves_en_estudio
  
  def realizarRutinaSobreAves(self):
    for ave in self.aves_en_estudio:
        ave.alimentacion(80)
        ave.volar(70)
        ave.alimentacion(10)

    def avesEnEquilibrio(self):
        for ave in self.aves_en_estudio:
            if ave.esta_en_equilibrio():
                return ave

class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
        self.energia = self.energia + 4 * gramos

    def volar(self, kms):
        self.energia -= 10 + kms

    def esta_en_equilibrio(self):
        return self.energia < 300 and self.energia > 150

    def alimentacion(self, gramos):
        self.comer_alpiste(gramos)

class Gorrion:
    def __init__(self, energia):
        self.energia = energia
  
    def comer_avena(self, gramos):
        self.energia = self.energia + 0.5 * gramos

    def volar(self, kms):
        self.energia -= 2 * kms

    def esta_en_equilibrio(self):
        return self.energia < 300 and self.energia > 150

    def alimentacion(self, gramos):
        self.comer_avena(gramos)

perry=Ornitologo()
phineas=Golondrina(500)
ferb=Golondrina(150)
isabella=Gorrion(300)
candance=Gorrion(750)


# Ejercicio 4
# Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:
# 
# comienzan con una cantidad que podemos establecer de combustible
# 
# los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido
# 
# las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;
# 
# pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible
# 
# saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.
# 
# Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.

# In[ ]:


class MedioDeTransporte:
    def cargar_combustible(self, litros):
        self.combustible+=litros
  
    def entran(self, personas):
        if self.lugares_libres>=personas:
            self.lugares_libres-=personas

    def cargar_combustible(self, litros):
        self.combustible+=litros

class Moto(MedioDeTransporte):
    def __init__(self, combustible):
        self.combustible=combustible
        self.lugares_libres=2

    def recorrer(self, kilometros):
        self.combustible-=0.5*kilometros

class Auto(MedioDeTransporte):
    def __init__(self,combustible):
        self.combustible=combustible
        self.lugares_libres=5

    def recorrer(self, kilometros):
        self.combustible-=kilometros

rayo=Auto(100)
mate=Auto(35)
guido=Moto(57)


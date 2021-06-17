```python
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
```


```python
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
```

¿Cuales son sus estados?

Los estados en ambas clases es alimento y caricias

¿Son polimorficas?

Comparten parte de la interfaz pero con distinta finalidad

¿Comparten su interfaz?

Podemos ver que comparten ciertas partes pero no por completo.
    La interfaz que comparten es energia, comer, acariciar y estaDebil.

¿Cuales son sus interfaces?

Son los conjuntos de metodos, por ende serian
    Las del gato, energia, comer, caricias, acariciar, estaDebil
    Las del perro, energia, comer, alimento, acariciar, estaDebil, pasear.
        

Ejercicio 2

Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este estado se alcanza cuando la energía se encuentra entre 150 y 300.


```python
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
    
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-f524547e7a71> in <module>
    ----> 1 class Golondrina(Ave): # Golondrina hereda de Ave
          2     def __init__(self, energia):
          3         self.energia = energia
          4 
          5     def comer_alpiste(self, gramos):
    

    NameError: name 'Ave' is not defined



```python

```

Clase 6 Practica

Ejercicio 1

Dada la siguiente clase, identificá la interfaz y el estado de la misma:

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

La interfaz son los mensajes que entiende un objeto, en este caso, la funcion energia, comer, acariciar y la funcion esta debil. Es decir, todos los metodos que tiene dicho objeto.

Por otro lado, el estado es el atributo dentro de cada constructor. Entonces, este es alimento y caricias.

Ejercicio 2

Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.


```python
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
    
  def nosepuedevolar(self, kms):
    if self.energia-(10 + kms)>=0:
        self.energia -= 10 + kms    
  

```

Ejercicio 3

Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.


```python
class Notebook:
    def __init__(self, marca, modelo, precio, numero):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
        self.numero=numero

    def aplicarDescuento(self, numero):
        descuento = (numero/100) * self.precio
        return (self.precio - descuento)
```


```python
computadora = Notebook("Asus", "Rog", 500, 500)
```


```python
computadora.aplicarDescuento()
```




    450.0



Ejercicio 4

Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:

inc()

dis()

reset()

valorActual()

valorNuevo(nuevoValor)

Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25



Ejercicio 5

Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".




```python
class Contador:
    def __init__ (self, valor_inicial):
        self.valor=valor_inicial
        self.comando= ""
    
    def inc(self):
        self.valor+=1
        self.comando = "incremento"
    
    def dis(self):
        self.valor-=1
        slef.comando = "disminucion"
    
    def reset(self):
        self.valor=0
        self.comando = "reset"
        
    def valorActual(self):
        print(self.valor)
                    
    def valorNuevo(self, valor_nuevo):
        self.valor=valor_nuevo
        self.comando = "actualizacion"
    
    def ultimoComando (self):
        print(self.comando)
```

Ejercicio 6
Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. Este objeto debe entender los siguientes mensajes:

cargar(numero)

sumar(numero)

restar(numero)

multiplicar(numero)

valorActual()


```python
def __init__(self,numero):
    self.numero = numero
    
    def cargar (self,numero):
        self.numero += numero
    def sumar (self, numero):
        self.numero += numero
    def restar (self, numero):
        self.numero -= numero
    def multiplicar (self, numero):
        self.numero *= numero
    def valorActual (self):
        print(self.valor)
```

Ejercicio 7

Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.


```python

```

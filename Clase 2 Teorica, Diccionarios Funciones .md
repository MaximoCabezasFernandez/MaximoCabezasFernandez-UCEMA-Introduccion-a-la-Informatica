```python
Clase 2 Teorica
```

Sindrome de Diogenes, donde la gente acumula cosas y no puede dejarlas

Las listas son mutables, se pueden modificar, se puede acceder por cada elemento de la lista, se hacen con corchetes y comas. Todo lo que esta dentro de la lista son int()


```python
list = [2,5,4]
```


```python
list
```




    [2, 5, 4]




```python
Se usa append para agregar elementos a la lista
Se usa remove para sacar cosas de la lista
```


```python
list.append('25')
```


```python
list.index('25')
```




    3



Index te permite saber el elemento en el que esta ubicado

Matryoshka de Datos

Diccionarios son mutables, pero, no poseen orden, no se usa index. Se declaran usando "llave"


```python
diccionario = dict() 
```


```python
diccionario = {"llave":"valor"}
```


```python
diccionario
```




    {'llave': 'valor'}




```python
diccionario ["llave"]
```




    'valor'




```python
diccionario.keys()
```




    dict_keys(['llave'])




```python
comidas = {}
```


```python
comidas
```




    {}




```python
comidas["Frutas"] = ["Pera","Banana"]
```


```python
comidas["Frutas"]
```




    ['Pera', 'Banana']




```python
type(comidas["Frutas"])
```




    list



¿Como declarar una funcion?

Sirve para reciclar codigos a mayor escala

def funcion(argumento):
    operacion sobre el argumento
    return aqui va el resultado que quiero devolver


```python
def doble(numero):
    resultado = numero *2
    return resultado
```


```python
doble(4)
```




    8



Desafio 7


```python
def vaquita(precio,comensales):
    resultado = (precio/comensales)
    return resultado
```


```python
vaquita(120,2)
```




    60.0




```python
vaquita(700,5)
```




    140.0



Condiciones en Cada Funcion

if condicion:
    aqui van las ordenes que se ejecutan si la condicion es cierta
else:
    Aqui van las ordenes que se ejecutan si la condicion es falsa
    
Se crea utilizando(==,>, <,! =)


```python
def vaquita(precio,comensales):
    resultado = (precio/comensales)
    if resultado > 120:
        return  print("Uf re Caro")
    else:
        resultado < 70
        return print("Re Barato")
```


```python
vaquita(120,2)
```

    Re Barato
    


```python
vaquita(700,5)
```

    Uf re Caro
    

Bucles-For o pedidos

for elemento in lista:

    Para cada elemento en la lista...


```python
pedido = {"Ana" : "no veggie", "Paul" : "Veganas"}
```


```python
pedido ["Ana"]
```




    'no veggie'




```python
pedido.keys()
```




    dict_keys(['Ana', 'Paul'])




```python
lista_comensales = pedido.keys()
```


```python
for i in lista_comensales:
    print(i)
```

    Ana
    Paul
    


```python
print(pedido[i])
```

    Veganas
    


```python

```


```python

```

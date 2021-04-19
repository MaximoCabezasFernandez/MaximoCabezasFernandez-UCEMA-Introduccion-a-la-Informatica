Raw String

Teoria vimos distintos caracteres de escape
       ejemplo barra invertida
Hay que hacerle distinguir a python los distintos caracteres de escape
    Donde usamos la letra r para que interprete lo que nosotros queremos, al principio de cada expresion regular
    
Podemos usar el metodo de search que nos brinda "re", para obtener el string buscado y la posc donde se encuentra
    La unica condicion que quermos es que exista.
        Si buscamos y no hay nada, nos devuelve un "none"

import re
if re.search(patron, texto) is not None:
    bloque de codigo
else:
    bloque de codigo
    

Union de Rangos
    Es una manera abreviada de escribir una serie de caracteres los cuales van a formar parte de nuestra expresion regular, para buscarlos o ignorarlos
    Usabamos al inicio y fin del rasngo entre corchetes y separados entre guion.
    Para ignorar el rango utilizabamos el caracter "^".

Ademas, usabamos el group() y el findall()
    El group() nos devuelve la coincidencia, sin embargo si quremos encontrar un patron en particular hay que modificar el texto


```python
import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit"
re.search(patron, texto).group()
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
re.search(patron, texto).group(0)
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
re.search(patron, texto).group(1)
' dolor sit amet, consectetur ipsum elit. Amet '
```




    ' dolor sit amet, consectetur ipsum elit. Amet '



Acá se utilizaron algunos metacaracteres, como lo son el punto (.) para indicar que puede ser cualquier carácter, y el asterísco (*) para indicar que puede haber 0 o más de estos caracteres

Existe una forma de priorizar los matches internos y es con el metacarácter ?


```python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = "ipsum(.*?)sit"
>>> re.search(patron, texto).group()
'ipsum dolor sit'
>>> re.search(patron, texto).group(0)
'ipsum dolor sit'
>>> re.search(patron, texto).group(1)
' dolor  '
```




    ' dolor  '



Cuando se quiere obtener todas las apariciones del patron se utiliza el metodo findall el cual actua para cada coincidencia somo si devolviera el group(1)
    Es decir devuelve en una lista la parte que se encuentra dentro de los delimitadores


```python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = "ipsum(.*?)sit"
>>> re.findall(patron, texto)
[' dolor ', ' elit. Amet ']
```




    [' dolor ', ' elit. Amet ']



Con las expresiones regulares se puede utilizar un metacarácter \b el cual delimita caracteres alfanúmericos de otros que no lo son. 
    De esta manera podemos obtener las palabras de alguna frase 
        Si delimitamos la búsqueda con este metacarácter al inicio y al final


```python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = r"\bipsum\b"
>>> re.sub(patron, "lapsus", texto)
re.sub(patron, "lapsus", texto)
```




    'Lorem lapsus dolor sit amet, consectetur lapsus elit. Amet sit amet.'



Ejercicio 1 TP 3

Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son az, AZ y 0-9.


```python
import re
```


```python
texto =  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet"
```


```python
patron = "[a-zA-Z0-9]"
```


```python
def programa_verificado (patron,texto):
    if re.search (patron,texto):
        print("Verificado")
    else:
        print("No Verificado")  
        
```


```python
programa_verificado(patron,texto)
```

    Verificado
    

Ejercicio 2

Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.


```python
texto ="[a-zA-Z0-9]"
patron = "[a-zA-Z0-9]"
```


```python
def programa_verificado2 (patron, texto):
    if re.findall (patron,texto):
        print("Verificado")
    else:
        print("No Verificado")
```


```python
programa_verificado2 (patron,texto)
```

    Verificado
    

Ejercicio 3 TP 3


```python
import re
```


```python
import re

def dos_P (lista):
    for elemento in lista:
        resultado = re.match (("(P\w*)\W(P)\W*"), elemento)
        if resultado is not None:
            print(resultado.group())
lista = (["Práctica Python", "Práctica C++", "Práctica Fortran"])
```

Ejercicio 4


```python
import re
```


```python
st =input("Escribi un String sin espacios: ")
for t in st:
    if "_" in st:
        print("Existe un guion bajo")
else:
    if "_" not in st:
        print("No existe un guion bajo")
```

    Escribi un String sin espacios: holacabezadecaca
    No existe un guion bajo
    

Ejercicio 5


```python
num =input("Tenes 2 opciones para escribir este string, con un numero adelante o no: ")
```


```python
for n in num:
    if "[0-9]" in num:
        print("Este string arranca con un numero")
else:
    if "[0-9]" not in st:
        print("Este string no arranca con un numero")
```

Ejercicio 6 TP 3


```python
import re
```


```python
patron = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet"
texto = "[a-zA-Z0-9- ]"
```


```python
busqueda = re.search(patron, texto)
if texto in patron:
        print("Este texto es valido")

```


```python
print(busqueda)
```

    None
    

Ejercicio 7


```python
import re
```


```python
st1 = input("Escribi un texto: ")
patron1 = "[a-zA-Z0-9- ]"
```


```python
def txt (st1):
    if re.search(patron1, st1) is not None:
        print("No se encontro ninguna de las variantes")
    else:
        print("Se encontro alguna de las variables")
```

Ejercicio 8


```python
import re
string = input("Ingrese un texto:")
patron = "\d"
lista = re.findall(patron, string)
for i in lista:
    print(int(i))
```

Ejercicio 9


```python

```

Ejercicio 11 TP 3


```python
def encontrar_patron(string):
    patron = "he*"
    if re.search (patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron)
```


```python
dos_P(lista)
```

    Práctica P
    


```python
Ejercicio 7
```

Ejercicio 13


```python

```

Ejercicio 14


```python
text = input("Escribi el texto que quieras: ")
newtext = text.replace(" ", ";")
newtext
```

    Escribi el texto que quieras: "Realizá un programa que reemplace los espacios y tabulaciones por punto y coma"
    




    '"Realizá;un;programa;que;reemplace;los;espacios;y;tabulaciones;por;punto;y;coma"'



Ejercicio 15


```python
correo= input("Decime tu Correo Electronico: ")
if "@" in correo:
    print("Es Valido")
else:
    print("No es Valido")
```

    Decime tu Correo Electronico: machu.cabezas@outlook.com
    Es Valido
    


```python

```

Expresiones Regulares

Lo esencial es invisible a los ojos

Secuencia de escapes, son una combinacion de caracteres que tiene un significado distinto de los caracteres literales contenidos en ella
    Se usa para definir ciertos caracteres especiales
        por ejemplo, escribir una palabra entre asteriscos en WPP
  Combinaciones tipicas constan de una barra invertida (\) el salto de linea.
\n - Salto de Linea
\t - Tab o cambio de pestaña
\s - Espacio
' - Comillas Simples
" - Comillas Dobles
  


```python
import re
```


```python
import pandas as pd
```

¿Que son las expresiones regulares?

Son cadenas de caracteres basadas en reglas sintacticas, permiten describir secuencias de caracteres.
    Es decir, es un criterio para buscar, capturar o reemplazar texto utilizando patrones. 
Se pueden concatenar para formar nuevas expresiones regulares, A y B son expresiones regulares AB tambien es.


Metacaracteres

Son caracteres especiales que, segun su contexto, tienen un significado especial para las expresiones regulares
    Metacaracteres delimitadores
        Nos permite delimitar donde queremos buscar los patrones de busqueda
^ - Inicio de Linea
$ - Fin de Linea
\A - Inicio de Texto
\Z - Fin de Texto
. - Coincide con cualquier carater de una linea dada. 
        Antes definiendo el Texto
        PARA QUE FUNCIONE SE TIENE QUE USAR COMO PRINT()


```python
texto  =  'Esta es la linea uno\npalabra en la linea dos\n'
```


```python
print(texto)
```

    Esta es la linea uno
    palabra en la linea dos
    
    

Para Pensar (1)

Expresion Regular A - Verdadero
Expresion Regular B - Falso
Expresion Regular C - Falso
Expresion Regular D - Falso

Tambien se nos permite repetir cierta cantidad de veces una busqueda dada
    Se utilizan los
        Metacaracteres Cuantificadores
* - Cero o Mas: Todas las ocurrencias de un dado substring
+ - Una o Mas ocurrencias del patron
? - Cero o Una
(n} - Exactamente n veces
(n;m) - Por lo menos n pero no mas de m veces
        

Para Pensar (2)

"X(.*)Y" La experesion se leeria de la siguiente manera

Buscar un substring que empieze con una x y termine con y y dentro tenga cualquier cosa

Desafio 1
\ d {4,}

Desafio 2
[az] {3,6}

Desafio 3
ab *

Existen otro tipo de Metacaracteres Predefinidos

\w - Caracter Alfanumerico
\W - Caracter NO Alfanumerico
\d - Caracter Numerico
\D - Caracter NO Numerico
\s - Un espacio, de cualquier tipo (t\n\r\f)
\S - Cualquier caracter que no sea espacio

Rangos

Es una clase de caracteres abreviada que se crea el primer caracter del rango, un guion/2 puntos, y el ultimo caracter del rango

- El rango [a-d] equivale al [abcd]
- El rango [1-10] equivale al substring [12345678910]
- El rango [Dd] equivale a buscar una D mayúscula y una d minúscula

Desafio 4 /d+

Coincidencias o Partidos

Los Caracteres Coincidentes
    Si un string se corresponde con el criterio que define una expresion regular, se dice que el String hace coincidir con la expresion; y equivalentemente, se dice que la expresion acepta el string
Span = Te dice donde esta en el texto
Podemos encontrar patrones usando el Search:



```python
import re
texto =  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet"
patrón  =  "amet" 
```


```python
re.search(patrón,texto)
```




    <re.Match object; span=(22, 26), match='amet'>




```python
busqueda = re.search (patrón,texto)
```


```python
print(busqueda)
```

    <re.Match object; span=(22, 26), match='amet'>
    


```python
texto[22:26]
```




    'amet'



Ahora veamos que hace match(), re busca el patron y devuelve la primera aparicion y solo al principio de la cadena

Si se encuentra una coincidencia en la primera linea, devuelve el objeto de coincidencia
Pero, si se enceuntra una coincidencia en alguna otra linea , devuelve un valor nulo.


```python
re.match(patrón,texto)
```


```python
busqueda2 = re.match(patrón,texto)
```


```python
print(busqueda2)
```

    None
    


```python
re.search(patrón,texto).group()
```




    'amet'



Otro metodo que nos permite obtener todas las ocurrencias del substring "Amet"


```python
re.findall(patrón,texto)
```




    ['amet', 'amet']



Funcion Sub

Permite reemplazar todas las ocurrencias del patron por otro patron en un String


```python
re.sub(patrón,"###",texto)
```




    'Lorem ipsum dolor sit ###, consectetur adipiscing elit. Amet et ###'



https://regexr.com/
https://www.freeformatter.com/regex-tester.html
https://docs.python.org/3/library/re.html

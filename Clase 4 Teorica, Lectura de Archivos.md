Lectura y escritura de archivos con Python

1. Archivos

Python tiene la cap de acceder y realizar operaciones de lectura/escritura sobre los documentos localizados en un sistema de archivos.

Para Python existen 2 tipos de archivos: Texto o Binarios. Se manipulan de modos distintos

Binario, es cualquier tipo de archivo que no es uno de texto, necesita se leido o interpretado por aplicaciones

Texto, formados por secuencia de lineas, donde cada linea incluye una secuencia de caracteres, donde se utilizan distintos tipos de caracteres especiales, como (\n)

2. Apertura de Archivos

Para abrir un archivo de texto, se puede usar el open()


```python
open(path_al_archivo, modo) EJEMPLO
```

"path_al_archivo" es un objeto de tipo str que indica la ruta en la quie se encuentra el archivo

"modo" es un objeto tipo str que indica la forma en la que Python accedera al archivo en cuestion

Existen distintos tipos de apertura de archivos

r ----> abre un archivo solo para lectura
r+ ----> abre un archivo para lectura y escritura
a ----> abre un archivo para agregar informacion. Si el archivo no existe, crea un nuevo archivo para escritura
w ----> abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe crea  un nuevo archivo para escritura. 

3. Cierre de Archivos

Es importante cerrarlos por diferentes motivos

Dejar archivos abierto
    Pone al archivo en manos de los "recolectores de basura"
    Se relentiza la maquina
    Muchos cambios no entran en vigencia hasta que lo cierren.


```python
archivo = open(path_al_archivo, modo)
archivo.close()
```

Existe otra forma de cerrar el archivo


```python
with open(path_al_archivo, modo) as miarch:
    Aca van las lineas de procesamiento del archivo
```

4. Rutas absolutas y relativas

Sera entonces el recorrido de directorios o carpetas que debmos recorrer para llegar a nuestro archivo. Se escribe seprando por barras invertidas. Esto es la ruta Absoluta.


```python
windows "C:\Users\PC\Documents\Rockstar_Games\Launcher\Profiles\39DFE977"
```


```python
import glob as gb
```


```python
import os as os
```

Esta biblioteca del sistema operativo de Python proporciona funciones para interactuar con el sistema operativo. Esta incluye métodos que como os.getcwd() o os.chdir(), que nos permitirá conocer el directorio de trabajo o cambiar de directorio de forma automática:

Estas son librerias de archivos

Ademas, se puede abrir rutas relativas
    Distintas maneras de llegar a donde queremos ir


```python
ls ./Fundamentos/Manipulación_de_archivos.md
```


```python
Desafio 1
```


```python
import re
```


```python
text = open(r"C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt", "r")
```


```python
print(text.read())
```

    Miradnos.
    Somos la luz de nuestra propia sombra,
    el reflejo de la carne que nos ha acompaÃ±ado,
    la fuerza que impulsa a las olas mÃ¡s minÃºsculas.
    
    Somos el azar de lo oportuno,
    la paz que termina con las guerras ajenas,
    dos rodillas araÃ±adas que resisten con valentÃ­a.
    
    Miradnos.
    Decidimos cambiar la direcciÃ³n del puÃ±o
    porque nosotras no nos defendemos:
    nosotras luchamos.
    
    Miradnos.
    Somos, tambiÃ©n, dolor,
    somos miedo,
    somos un tropiezo fruto de la zancadilla de otro
    que pretende marcar un camino que no existe.
    Somos, tambiÃ©n, una espalda torcida,
    una mirada maltratada, una piel obligada,
    pero la misma mano que alzamos
    abre todas las puertas,
    la misma boca con la que negamos
    hace que el mundo avance,
    y somos las Ãºnicas capaces de enseÃ±ar
    a un pÃ¡jaro a volar.
    
    Miradnos.
    Somos mÃºsica,
    inabarcables, invencibles, incontenibles, inhabitables,
    luz en un lugar que aÃºn no es capaz de
    abarcarnos, vencernos, contenernos, habitarnos,
    porque la belleza siempre cegÃ³ los ojos
    de aquel que no sabÃ­a mirar.
    
    Nuestro animal es una bestia indomable
    que dormÃ­a tranquila hasta que decidisteis
    abrirle los ojos con vuestros palos,
    con vuestros insultos, con este desprecio
    que, oÃ­dnos:
    no aceptamos.
    
    Miradnos.
    Porque yo lo he visto en nuestros ojos,
    lo he visto cuando nos reconocemos humanas
    en esta selva que no siempre nos comprende
    pero que hemos conquistado.
    
    He visto en nosotras
    la armonÃ­a de la vida y de la muerte,
    la quietud del cielo y del suelo,
    la uniÃ³n del comienzo y del fin,
    el fuego de la nieve y la madera,
    la libertad del sÃ­ y el no,
    el valor de quien llega y quien se va,
    el don de quien puede y lo consigue.
    
    Miradnos,
    y nunca olvidÃ©is que el universo y la luz
    salen de nuestras piernas.
    
    Porque un mundo sin mujeres
    no es mÃ¡s que un mundo vacÃ­o y a oscuras.
    Y nosotras
    estamos aquÃ­
    para despertaros
    y encender la mecha.
    
    - Elvira Sastre -
    


```python
texto1 =text.read() 
```


```python
patron = "-(.*)-"
```


```python
print(re.search(patron, texto1))
```

    None
    

Desafio 2


```python
open(r"C:\Users\PC\OneDrive\UCEMA\1er Semestre (2AÑO)\PRINCIPIOS DE INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\bio.txt", "a")
```




    <_io.TextIOWrapper name='C:\\Users\\PC\\OneDrive\\UCEMA\\1er Semestre (2AÑO)\\PRINCIPIOS DE INFORMATICA\\UCEMA_Fundamentos_de_informatica-master\\Python_intro\\bio.txt' mode='a' encoding='cp1252'>



5. Lectura y escritura de Archivos

La escritura de los archivos en Python se hace de forma sencilla con el método write(), que toma como parámetro un string con el contenido que desamos almacenar en el archivo:



```python
with open(path_al_archivo, modo) as miarch:
    miarch.write("Este es el contenido del archivo")
```

Se puede abrir y leer de esta manera.

bio = open("bio.txt", "r")
bio.read()

.read() Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.

.readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa.

.readlines() Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista.

Manejo de Excepciones

2. Syntax Error

Cuando existen errores en el codigo se detiene el programa.

>>> print(Hola mundo')
  File "<stdin>", line 1
    print(Hola mundo')
               ^
SyntaxError: invalid syntax
    
Cada error nos dice un mensaje de informacion que nos permite encontrar el origen del problema

3. Excepciones

No son errores sintacticos y nos dicen que error es el que esta occuriendo. 
    
>>> 3 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
    
>>> print(divisor)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'divisor' is not defined

    

Desafio 1


```python
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d)/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
```


      File "<ipython-input-21-0b19574cc415>", line 12
        sol2 = (-b+cmath.sqrt(d))/(2*a)
        ^
    SyntaxError: invalid syntax
    


Al ejecutar el programa tenemos un error del tipo "SyntaxError:", que nos indica que en nuestro programa tiene un error sintactico.
Este mismo se encuentra en la linea 12 del programa. Al ejecutar el programa con el error incluido, aparte del tipo de error nos dice donde se encuentra.

Desafio 2


```python
>>> print(divisor)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-25-f15ad749f1c9> in <module>
    ----> 1 print(divisor)
          2 
    

    NameError: name 'divisor' is not defined


Este error nos indica que hay un error de tipo "NameError", donde previamente al ejecutar el programa no definimos la variable "divisor"


```python
3 / 0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-26-e1965806ec03> in <module>
    ----> 1 3 / 0
    

    ZeroDivisionError: division by zero


En cuanto a este programa estamos obteniendo como resultado el error tipo "ZeroDivisionError", que nos muestra que no se puede dividir por 0

Desafio 3


```python
0 + "2"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-27-598b32311c9f> in <module>
    ----> 1 0 + "2"
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'


Por otro lado, este error es de tipo "TypeError", que nos aclara que no se puede sumar una variable de tipo "str", debe ser una variable de int

4. Con intentar no perdemos nada

Para el manejo de excepciones Python nos brinda unas palabras reservadas, nos permite manejar las excepciones que pueden surgir y tomar acciones que evitan la interrupcion del programa

Una de las palabras reservadas es try
        Nos permite encapsular un bloque de codigo para interceptar e identificar excepciones.

Si se produce un error dentro de la declaracion try-except, se omite una excepcion y se ejecutaa el bloque de codigo que maneja dicha excepcion.


try:
    # aquí ponemos el código que puede lanzar excepciones
except:
    # entrará aquí en caso que se haya producido una excepción


```python
def mitad(numero):
    return(numero/2)
```


```python
print(mitad(3))
print(mitad(0))
```

    1.5
    0.0
    


```python
def division(numero,divisor):
    try:
        return(numero/divisor)
    except:
        print("Ops! Hoy estoy qumado")
print(division(3,2))
print(division(2,0))

```

    1.5
    Ops! Hoy estoy qumado
    None
    

5. Excepciones Personalizadas

En algunos casos, puede ser necesario crear excepciones personalizadas o forzar que ocurra una excepcin especifica dado un contexto.

La sentencia raise se puede indicar el tipo de excepcion que deseamos lanzar y el mensaje de que queremos brindarle al usuario


```python
def check_int_type():
    if type(x) != int:
        raise TypeError ("Only integers are allowed")
```


```python

```

El uso del if/else

Para tomar decisiones donde se hace una cosa u la otra
    if condicion:
        Ordenes si la condicion es verdadera
    else:
        Ordenes si la condicion es falsa
        
¿Que pasa si hay 2 condiciones?
    if condicion1:
        ordenes si la condicion1 es verdadera
    else:
        if condicion2:
            Ordenes si la condicion2 es verdadera
    
   if condicion1:
        ordenes si la condicion1 es verdadera
    else:
        if condicion2:
            Ordenes si la condicion2 es verdadera
        else:
            ordenes si ninguna condicion es verdadera
Se usa "elif"

   if condicion1:
       ordenes si la condicional es verdadera
   elif condicion2:
       ordenes si la condicional es falsa y la condicion2 es verdadera
   else:
       ordenes si la condicion es falsa
       
Repeticiones

Sabiendo la cantidad de repeticiones: "for"
    for variable in iterable(se puede separar en elementos):
        ordenes a repeteir
Iterable
    String
    Range
    Lista
    Diccionario
    
   for letra in "Hola:
        Print(letra)
   H
   O
   L
   A
   
   For numero in range(5):
       print (numero)
   0
   1
   2
   3
   4

Repeticiones

Sin saber la cantridad de repeticiones: "while"
    while condicion:
        ordenes a repetir     
   Importante
       Dentro de las ordenes que se repiten tiene que haber una que me modifique la condicion, a fin de evitar un bucle infinito

contador = 0
while contador <3:
    print (contador)
    contador = +1 



```python
import re
```


```python
import pandas as pd
```

Ejercicio 1

Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.


```python
def letra (cadena):
    if (cadena[0]).isupper() == True:
        print("la primer letra es mayuscula")
    else:
        print("la primer letra es minuscula")
        
```


```python
letra ("Machu")
```

    la primer letra es mayuscula
    


```python
letra ("machu")
```

    la primer letra es minuscula
    

Ejercicio 2

Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).


```python
def QueNumeroEs(numero):
    if abs (numero) == numero:
        print("es positivo")
    elif numero == 0:
        print ("es cero")
    else:
        print("es negativo")      
```


```python
QueNumeroEs (-7)
```

    es negativo
    

Ejercicio 3


```python
numero = int(input("Ingrese un numero del 1 al 6:"))
if numero >=1 and numero <= 6:
    print (7 - numero)
else:
    print("el numero ingresado es incorrercto")
```

    Ingrese un numero del 1 al 6:3
    4
    

Ejercicio 4


```python
gramos = int(input("Ingrese el peso en gramos: "))
zona = input("Ingrese la zona: ")
if gramos <5000:
    if zona == "America del Sur":
        print(10 * gramos)
    elif zona == "America Central":
        print(15 * gramos)
    elif zona == "America del Norte":
        print(18 * gramos)
    elif zona == "Europa":
        print(24 * gramos)
    elif zona == "Asia":
        print(30 * gramos)
else:
    print ("Su paquete fue rechazado")
        
        
```

    Ingrese el peso en gramos: 541
    Ingrese la zona: Asia
    16230
    

Ejercicio 5


```python
def QueDiaEsHoy (dia):
    if dia() == "1":
        print("Hoy es Lunes")
    elif dia() == "2":
        print("Hoy es Martes")
    elif dia() == "3":
        print("Hoy es Miercoles")
    elif dia() == "4":
        print("Hoy es Jueves")
    elif dia() == "5":
        print("Hoy es Viernes")
    elif dia() == "6":
        print("Hoy es Sabado")
    elif dia() == "7":
        print("Hoy es Domingo")
```


```python
QueDiaEsHoy = int(input("Ingrese el dia de la semana en numero: "))

if QueDiaEsHoy == 1:
    print("Hoy es Lunes")
if QueDiaEsHoy == 2:
    print("Hoy es Martes")
if QueDiaEsHoy == 3:
    print("Hoy es Miercoles")
if QueDiaEsHoy == 4:
    print("Hoy es Jueves")
if QueDiaEsHoy == 5:
    print("Hoy es Viernes")
if QueDiaEsHoy == 6:
    print("Hoy es Sabado")
if QueDiaEsHoy == 7:
    print("Hoy es Domingo")   
if QueDiaEsHoy > 7:
    print("No hay mas de 7 dias chinchulin")
```

    Ingrese el dia de la semana en numero: 9
    No hay mas de 7 dias chinchulin
    

Ejercicio 6

Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.


```python
a1 = input("Dame un elemento:")
a2 = input("Dame un elemento:")
a3 = input("Dame un elemento:")
a4 = input("Dame un elemento:")
a5 = input("Dame un elemento:")
```


```python
lista [a1,a2,a3,a4,a5]
for item in lista [::-1]:
    print (item)
lista2=list(lista)
lista2.reverse()
print(lista2)
```

Ejercicio 7


```python
lista = []
numero = int(input("Introduce un número en la lista:"))
while numero>=0:
    lista.append(numero)
    numero = int(input("Introduce un número en la lista:"))

for numero in lista:
    print(numero," ",end="")

```

    Introduce un número en la lista:1
    Introduce un número en la lista:2
    Introduce un número en la lista:3
    Introduce un número en la lista:4
    Introduce un número en la lista:5
    Introduce un número en la lista:-6
    1  2  3  4  5  

Ejercicio 8


```python
lista1 = []
lista2 = []
lista3 = []
for index in range(1,6):
    lista1.append(int(input("Introduce el elemento %d del valor1:" % index)))
for index in range(1,6):
    lista2.append(int(input("Introduce el elemento %d del valor2:" % index)))

for index in range(0,5):
    lista3.append(lista1[index] + lista2[index])

print("La suma de los valores es:")
for numero in lista3:
    print(numero," ",end="")

```

Ejercicio 9


```python

nombres = []
edades = []
while True:
    nombre = input("Dime el nombre de un alumno:")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime su edad:")))
    if nombre == "*": break;

edad_max = max(edades)

print("Alumnos menores de edad")
print("=======================")
for nombre,edad in zip(nombres,edades):
    if edad >= 18:
        print(nombre)
print("Alumnos mayores")
print("===============")
for nombre,edad in zip(nombres,edades):
    if edad == edad_max:
        print(nombre)

```

    Dime el nombre de un alumno:Maximo
    Dime su edad:19
    Dime el nombre de un alumno:Joaquin
    Dime su edad:23
    Dime el nombre de un alumno:Felicitas
    Dime su edad:17
    Dime el nombre de un alumno:*
    Alumnos menores de edad
    =======================
    Maximo
    Joaquin
    Alumnos mayores
    ===============
    Joaquin
    

Ejercicio 10


```python
import re
```


```python
contadores = {}
```


```python
cadena = input("Escribi una cadena: ")
for caracter in cadena:
    if caracter in contadores:
        contadores[caracter]+=1
    else:
         contadores[caracter]=1

```

Ejercicio 11


```python
cnt = {}
alph = "qwertyuiopasdfghjklñzxcvbnm"
for l in alph + alph.upper():
    cnt[l] = 0
ch = input("Insertar string: ")
for c in ch:
    if c.lower() in alph:
        cnt[c] += 1
for ky, vl in cnt.items():
    print(ky,vl)
```

    Insertar string: "Machu"
    q 0
    w 0
    e 0
    r 0
    t 0
    y 0
    u 1
    i 0
    o 0
    p 0
    a 1
    s 0
    d 0
    f 0
    g 0
    h 1
    j 0
    k 0
    l 0
    ñ 0
    z 0
    x 0
    c 1
    v 0
    b 0
    n 0
    m 0
    Q 0
    W 0
    E 0
    R 0
    T 0
    Y 0
    U 0
    I 0
    O 0
    P 0
    A 0
    S 0
    D 0
    F 0
    G 0
    H 0
    J 0
    K 0
    L 0
    Ñ 0
    Z 0
    X 0
    C 0
    V 0
    B 0
    N 0
    M 1
    

Ejercicio 12


```python
mrks = {}
qnt = int(input("Cantidad de alumnos: "))
nm = ""
mrk = 0
for i in range(qnt):
    mrklist = []
    nm = input("Nombre: ")
    mrk = int(input("Nota: "))
    if nm not in mrks.keys():
       while mrk > 0:
            mrklist.append(mrk)
            mrks[nm] = mrklist
            mrk = int(input("Nota: "))
            print(mrklist)
    else:
        print("Alumno ya cargado")

for nm in mrks.keys(): 
    marks = 0
    qn = 0
    for ex in mrks[nm]:
        marks += ex
        qn += 1
    print("Promdedio de: ", nm, ":", marks/qn)
```

    Cantidad de alumnos: 18
    Nombre: Maximo
    Nota: 10
    Nota: 9
    [10]
    

Ejercicio 13


```python
def esMultiplo(n1,n2):
    if n1 % n2 == 0:
        print(n1, " es multiplo de ", n2)
    elif n2 % n1 == 0: 
        print(n2, " es multiplo de ", n1)
    else:
        print("No son multiplos")

num1 = int(input("Primer numero entero: "))
num2 = int(input("Segundo numero entero: "))
```

    Primer numero entero: 8
    Segundo numero entero: 4
    


```python
esMultiplo(8,4)
```

    8  es multiplo de  4
    

Ejercicio 14


```python
def medTemp(min, max):
    return (min+max)/2

qnt = int(input("Cantidad de días: "))
days = {}

for day in range(qnt):
    mn = int(input("Temperatura mínima: "))
    mx = int(input("Temperatura máxima: "))
    mt = medTemp(mn,mx)
    days[day+1] = mt

print(days)
```

    Cantidad de días: 20
    Temperatura mínima: 10
    Temperatura máxima: 20
    Temperatura mínima: 10
    Temperatura máxima: 20
    Temperatura mínima: 10
    Temperatura máxima: 20
    

Ejercicio 15


```python
  
members = [
    {
        "Socio número" : 1,
        "Nombre" : "Florencia Ocampo",
        "Fecha de ingreso" : "14/09/2001",
        "Cuota al día" : True

    },
    {
        "Socio número" : 2,
        "Nombre" : "David Estévez",
        "Fecha de ingreso" : "14/09/2001",
        "Cuota al día" : True
    },
    {
        "Socio número" : 3,
        "Nombre" : "Sofía Cáceres",
        "Fecha de ingreso" : "14/09/2001",
        "Cuota al día" : True
    }
]

def howMany():
    return len(members)

def addMember():
    num = howMany() + 1
    name = input("Nombre: ")
    date = input("Fecha de ingreso: ")
    members.append({
        "Socio número" : num,
        "Nombre" : name,
        "Fecha de ingreso" : date,
        "Cuota al día" : True
    })
    #printMembers()
  
def feeCorr():
    n = int(input("Número de socio: "))
    i = n + 1
    member = members[i]
    fee = member.get("Cuota al día")
    if fee:
        print("Las cuotas están todas al día")
    else:
        print("Las cuotas no están al día")

def changeDate():
    for member in members:
        date = member.get("Fecha de ingreso")
        if date == "21/10/2017":
            date = "22/10/2017"

def terminateMembership():
    name = input("Nombre y apellido de socio: ")
    for member in members:
        n = member.get("Nombre")
        if n == name:
            members.remove(member)
    #printMembers()

def printMembers():
    for member in members:
        name = member.get("Nombre")
        print(name)

print("¿Qué acción desea realizar?")
print("1 - Agregar miembro")
print("2 - Obtener cantidad de miembros totales")
print("3 - Corroborar las cuotas de un miembro")
print("4 - Dar de baja a un miembro")
print("5 - Ver listado de miembros")
quest = input("Inserte el número correspondiente a la acción: ")

if quest == "1":
    addMember()
elif quest == "2":
    print(howMany())
elif quest == "3":
    feeCorr()
elif quest == "4":
    terminateMembership()
elif quest == "5":
    printMembers()
else:
    print("Error, vuelva a intentar insertar un número del 1-5")
```


```python

```

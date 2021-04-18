Ejercicio 1


```python
string = input("Ingrese una Palabra:")
```

    Ingrese una Palabra:Defensa y Justicia
    


```python
print(len(string)) 
```

    18
    

Ejercicio 2


```python
string2 = input("Ingrese una palabra de al menos 10 letras: ")
```

    Ingrese una palabra de al menos 10 letras: Defensa y Justicia
    


```python
print(string2.upper()[4:6])
```

    NS
    

Ejercicio 3


```python
nombre = input("Buenas, dime tu nombre: ")
input("Decime tu Edad: ")
print("Mucho Gusto")
```

    Buenas, dime tu nombre: Maximo
    Decime tu Edad: 19
    Mucho Gusto
    

Ejercicio 4


```python
nombre2 = input("Buen dia, ingrese su nombre y apellido completo porfavor: ")
nombre2 = nombre2.upper()
n_list = nombre2.split()
for nombre2 in n_list:
    print(nombre2[0])
```

    Buen dia, ingrese su nombre y apellido completo porfavor: Maximo Cabezas Fernandez
    M
    C
    F
    

Ejercicio 5


```python
contador = 0
suma = 0
numero = 1
```


```python
while numero != 0:
    numero = int(input("Decime un numero entero (0 para terminar de usar programa: "))
    
if numero !=0:
    suma += numero
    contador +=1

```


```python
if contador ==0:
    print("No digito ningun numero.")
else:
    promedio = suma/contador
    
    print("El promedio de los {} numeros es igual a {}.".format(contador,promedio))
```

    No digito ningun numero.
    

Ejercicio 6


```python
cant_minutos = int(input("Ingrese cantidad de minutos: "))
print (cant_minutos//60, "horas y", (cant_minutos % 60), "minutos")
```

    Ingrese cantidad de minutos: 10
    0 horas y 10 minutos
    

Ejercicio 7


```python
sueldo_base = int(1000)
print(sueldo_base, "es el sueldo base del comerciante")

cant_ventas = int(4)
print(cant_ventas, "es la cantidad de ventas")

ingreso_por_venta = 250
print(ingreso_por_venta, "es el total de ingresos por venta")

def multiplicacion (ingreso_por_venta):
    resultado = ingreso_por_venta * 0.10
    return resultado 

monto_comision = multiplicacion (ingreso_por_venta)
print(monto_comision)

def multiplicacion (cant_ventas):
    resultado = cant_ventas * monto_comision
    return resultado

comision_por_ventas = multiplicacion (cant_ventas)
print(comision_por_ventas, "es el total de comisones por venta")    

def suma (sueldo_base):
    resultado = sueldo_base + comision_por_ventas
    return resultado 

total_dinero = suma(sueldo_base)
print(total_dinero, "es el total de dinero que ganara este mes el comerciante")
```

    1000 es el sueldo base del comerciante
    4 es la cantidad de ventas
    250 es el total de ingresos por venta
    25.0
    100.0 es el total de comisones por venta
    1100.0 es el total de dinero que ganara este mes el comerciante
    

Ejercicio 8


```python
correcta = int(input("Dame el número de respuestas correctas:"))
incorrecta = int(input("Dame el número de respuestas incorrectas:"))
en_blanco = int(input("Dame el número de respuestas en blanco:"))

def nota_final(correctas, incorrectas, en_blanco):
    nota = (correctas*4) + (incorrectas* -1)
    return nota

print(nota_final(correcta,incorrecta,en_blanco))
```

    Dame el número de respuestas correctas:3
    Dame el número de respuestas incorrectas:5
    Dame el número de respuestas en blanco:1
    7
    

Ejercicio Grupal


```python
def cuanto_tardo_en_pagar_deposito():
    costo_total=input("¿Cuánto vale la casa que te gustaría comprar? ")
    sueldo_anual=input("¿Cuál es tu sueldo anual? ")
    porcentaje_ahorrado=input("¿Qué porcentaje de tu sueldo ahorras por mes? ")
    sueldo_mensual=float(sueldo_anual)/12
    porcentaje_deposito=0.25
    ganancia_anual=0.04
    cantidad_ahorrada=0
    ahorro_mensual=float(porcentaje_ahorrado)*sueldo_mensual
    ganancia_mensual=ahorro_mensual*(ganancia/12)
    total_mensual=ahorro_mensual+ganancia_mensual
    deposito=float(costo_total)*porcentaje_deposito
    meses_para_deposito=round((deposito/total_mensual)+0.5)
    print("Te tomará "+str(meses_para_deposito)+" meses ahorrar el dinero necesario para pagar el depósito.")
```


```python

```


```python

```


```python

```

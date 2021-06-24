HTTP REST


```python
pip install requests
```

    Requirement already satisfied: requests in c:\programdata\anaconda3\lib\site-packages (2.24.0)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\programdata\anaconda3\lib\site-packages (from requests) (1.25.9)
    Requirement already satisfied: idna<3,>=2.5 in c:\programdata\anaconda3\lib\site-packages (from requests) (2.10)
    Requirement already satisfied: chardet<4,>=3.0.2 in c:\programdata\anaconda3\lib\site-packages (from requests) (3.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in c:\programdata\anaconda3\lib\site-packages (from requests) (2020.6.20)
    Note: you may need to restart the kernel to use updated packages.
    


```python
import requests
```

Tutorial Web

Internet se podria definir como la red de redes de computadoras, conectadas por medio de un cableado fisico que permite intercambiar info entre sus usuarios
    Para tener el servicio debemos tener 2 programas que se ejecuten en 2 computadoras diferentes
    La computadora que ejecuta el programa y proporciona la informacion se la denomina servidor. La computadora que consume esa informacion se la denomina cliente.

La Web
    En particular, diminutivo de World Wide Web, es un conjunto de paginas interconectadas por las cuales podemos navegar.
    Estas paginas web, estan pensadas para consumir contenido hipertextual, es decir contenido que vincule o enlaces contenidos.

Lenguajes Web
    HTML le da la estructura a la pagina, CSS le da el estilo y JS dinamiza la Pagina

Cloud Computing
    Consumo o prestacion bajo demanda de recursos tecnologicos a traves de internet
    Pagarle a un servidor para que me preste un servicio, ya que no tengo la plata para mantener un gran servidor

¿Para que necesitamos un protocolo de habla?

HTTP, es un protocolo que nos permite comunicar al cliente con el servidor.
    Donde nosotros le pedimos cosas para que realice sierta accion.
    Cada recurso de web es localizable gracias a un identificador llamado URL, Uniform Resource Locator. Vamos a hacer nuestro primer pedido.



```python
pip install requests
```

    Requirement already satisfied: requests in c:\programdata\anaconda3\lib\site-packages (2.24.0)
    Requirement already satisfied: chardet<4,>=3.0.2 in c:\programdata\anaconda3\lib\site-packages (from requests) (3.0.4)
    Requirement already satisfied: idna<3,>=2.5 in c:\programdata\anaconda3\lib\site-packages (from requests) (2.10)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\programdata\anaconda3\lib\site-packages (from requests) (1.25.9)
    Requirement already satisfied: certifi>=2017.4.17 in c:\programdata\anaconda3\lib\site-packages (from requests) (2020.6.20)
    Note: you may need to restart the kernel to use updated packages.
    


```python
import requests
```


```python
r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
```


```python
r.json()
```




    {'id': 1, 'tipo': 'pantalon', 'talle': 35}



Desafio 1


```python
r20 = requests.get('https://macowins-server.herokuapp.com/prendas/20')
```


```python
r.json()
```




    {'id': 1, 'tipo': 'pantalon', 'talle': 35}



Diccionario de lo que tiene el objeto

Si despues del json() usamos entre [] un criterio en este caso, tipo o id nos da lo que buscamos exactamente

Desafio 2


```python
r400 =  requests.get('https://macowins-server.herokuapp.com/prendas/400')
```


```python
r400.json()
```


    ---------------------------------------------------------------------------

    JSONDecodeError                           Traceback (most recent call last)

    <ipython-input-10-f8fef4a7645d> in <module>
    ----> 1 r400.json()
    

    C:\ProgramData\Anaconda3\lib\site-packages\requests\models.py in json(self, **kwargs)
        896                     # used.
        897                     pass
    --> 898         return complexjson.loads(self.text, **kwargs)
        899 
        900     @property
    

    C:\ProgramData\Anaconda3\lib\json\__init__.py in loads(s, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)
        355             parse_int is None and parse_float is None and
        356             parse_constant is None and object_pairs_hook is None and not kw):
    --> 357         return _default_decoder.decode(s)
        358     if cls is None:
        359         cls = JSONDecoder
    

    C:\ProgramData\Anaconda3\lib\json\decoder.py in decode(self, s, _w)
        335 
        336         """
    --> 337         obj, end = self.raw_decode(s, idx=_w(s, 0).end())
        338         end = _w(s, end).end()
        339         if end != len(s):
    

    C:\ProgramData\Anaconda3\lib\json\decoder.py in raw_decode(self, s, idx)
        353             obj, end = self.scan_once(s, idx)
        354         except StopIteration as err:
    --> 355             raise JSONDecodeError("Expecting value", s, err.value) from None
        356         return obj, end
    

    JSONDecodeError: Expecting value: line 1 column 1 (char 0)



```python
r400.headers
```

El Headers, nos permite ver el que tipo de datos estan en nuestro request.


```python
r.status_code
```

Desafio 3


```python
r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
```


```python
r.headers
```




    {'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '50', 'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 'Vary': 'Accept-Encoding', 'Date': 'Tue, 11 May 2021 16:54:09 GMT', 'Via': '1.1 vegur'}



Del headers podemos hacer lo mismo que en json, haccer type(r.headers) y nos da el tipo, pero r.headers[Content.Type] nos da lo que incluye a ello. 


```python
r.status_code
```

En los status_code, el numero 404 es un error y el 200 es que tiene la informacion y no hay error.


```python
r.status_code
```


```python
Desafio IV
```


```python
r = requests.get('https://macowins-server.herokuapp.com/prindas/1')
```


```python
r.headers
```


```python
r.status_code
```


```python
r.json()
```

Otro Codigo


```python
r = requests.get('https://macowins-server.herokuapp.com/nueva-funcionalidad-que-a-veces-no-anda-bien')
```


```python
r.headers
```


```python
r.content
```

Parametros

Vamos a cambiar un poco


```python
r = requests.get('https://macowins-server.herokuapp.com/prendas')
```


```python
r.json()
```


```python
r.content
```

El r.content nos muestra lo explicito

Desafio V


```python
r = requests.get('https://macowins-server.herokuapp.com/ventas')
```


```python
r.json()
```


```python
r = requests.get('https://macowins-server.herokuapp.com/ventas/2')
```


```python
r.json()
```

Tambien podemos filtrarlo segun el producto


```python
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon')
```


```python
r.json()
```


```python
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=saco')
```


```python
r.json()
```

Desafio VI


```python
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera')
```


```python
r.json()
```


```python
r = requests.get('https://macowins-server.herokuapp.com/prendas?talle=40')
```


```python
r.json()
```


```python
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon&talle=40')
```


```python
r.json()
```

Desafio VII


```python
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS')
```


```python
r.json()
```

URLs y URls

Una URL, en su primera parte nos muestra el protocolo, es cualquier string con un formato particular llamado URI nos permite localizar un recurso en internet. HTTPS = incriptado, HTTp = no incriptado

Las URIs se componente de:

Un protocolo
Un dominio
Opcionalmente, un puerto
Una ruta
Opcionalmente, parámetros
Opcionalmente, un fragmento, que indica en que sección queremos obtener del recurso que estamos consultando.

Ejemplo
   protocolo://dominio:puerto/ruta#fragmentoparametro1=valor1&parametro2=valor2

Una URI, es el por detras de una URL, donde seria la cabeza de la URL. La URI,seria el metodo de busqueda y la URL seria la busqueda en si.


Diseño de URLs

En genral el diseño de estas URLs se jace tal que cada ruta apunta a un recurso bien definido. La semantica de cada ruta esta dad en parte por el sentido propio en el contexto de ese dado dominio, pero tambien por le metodo HTTP que se utilice.

Ejemplo

- /productos/45: si se usa GET, se devuelve el producto con id 45. Si se usa DELETE, se lo borra. 

- /productos: si se usa GET devuelve todos los productos, si se usa PUT, se los actualiza en lote

- /productos/45/ventasRecientes: si se usa GET, devuelve todas las ventas recientes del producto con id 45

Creando y Actualizando

Ahora creamos una prenda, creamos en base al identificiador id.


```python
data = {'id': 'hola'}
```


```python
r = requests.post('https://macowins-server.herokuapp.com/prendas', data=data)
```


```python
r.json()
```




    {'id': 'hola'}



Como vemos, hay varios verbos (métodos) HTTP:

OPTIONS
GET
POST
PUT
PATCH
DELETE

Nada nos impide borrar con GET, eliminar con POST o consultar con PUT. ¡Son todas convenciones! Estas convenciones nos hablan de una semántica para cada uno de los verbos, y es importante respetarlas:

OPTIONS: consultar meta-datos o configuraciones de HTTP
GET: consultar un contenido sin efecto
POST: crear un contenido
PUT: actualizar de forma total un contenido
PATCH: actualizar de forma parcial un contenido
DELETE: eliminar un contenido

Recrusos

Normalización de REST: REST es un tipo de arquitectura de desarrollo web que se basa en el uso correcto de URLs y HTPP. Organizaremos nuestras rutas, tanto de una API como de un sitio común y corriente, en forma de recursos y colecciones.

GET /ventas/: consultar todos (listar)
DELETE /ventas/: borrar todos
POST /ventas/: crear uno
POST /ventas/1 crear uno con ID (QMP no lo soporta)
GET /ventas/1: consultar uno
PUT /ventas/1: modificar uno
DELETE /ventas/1: eliminar uno


Existen algunas reglas básicas para escribir las rutas REST:

Debe evitarse usar verbos
No debemos tener más de una URI para identificar un mismo recurso
Deben ser independiente de formato
Deben mantener una jerarquía lógica
Los filtrados de información de un recurso no se hacen en la URI

Desafio 1

Primero incluimos el Protocolo, Segundo un dominio como se va a llamar; creamos diferentes urls para distintos productos, 


```python
https://machu.com/libros ---> GET, POST
https://machu.com/revistas ---> GET, POST
https://machu.com/audiolibros ---> GET, POST
    
https://machu.com/libros/1 ---> GET, DELETE Y PUT
https://machu.com/revistas/1 ---> GET, DELETE Y PUT
https://machu.com/audiolibros/1 ---> GET, DELETE Y PUT

https://machu.com/libros
https://machu.com/revistas
https://machu.com/audiolibros
    
https://machu.com/libros
https://machu.com/revistas
https://machu.com/audiolibros
    
https://machu.com/libros
https://machu.com/revistas
https://machu.com/audiolibros
```

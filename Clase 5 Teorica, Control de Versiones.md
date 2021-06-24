Introduccion a la Programacion

Control de Versiones

   Se usa de forma colaborativa
       Los sistemas de control de versiones comienzan con una versiona base del documento y luego registran los cambios que realiza en cada paso del camino
       Se puede usar como un video
           Puede retroceder para comenzar en el doc inicial
           Reproducir cada estado o cambio que realizo
           Finalmente  a su version mas reciente

¿Que es un sistema de control de versiones?
    Seguir los cambios en un archivo
        Creando efectivamente diferentes versiones de nuestros archivos
    Cada registro de estos cambios se denomina commit y mantiene metadatos utiles
    El historial completo de commits para un proyecto en particular y sus metadatos forman un repositorio
    
¿Como funciona?
    Cada commit es un fotograma de nuestro video
        Funciona como un paquete de cambios realizados que se pueden ir agregando al stage
            Estado intermedio con cambios
            Mediante el comando gitt add
    Estos cambios se gestionan como una unidad, al generar un commit quedan regsitrados en una foto al hacer un git commit
    Importante destacar los cambios realizados
    Al hacer commit se obtiene un ID del mismo, que luego puede usarse en otros comandos para referenciar este bloque de cambios

Git al infinito y mas alla
    Trabaja con un repositorio local que esta en tu computadora
        Donde agregas tus commits y uno remoto
            Se puede subir tus commits, compartirlos
        Existen multiples Git
        
Podemos hacer una sincronizacion saliente del repo local al remoto.
    Haciedno Git Push
        Este comando envia los commits generados localmente que no se hayan enviado anteriormente
Podemos tambien descargar los cambios del repositorio remoto utilizando el comando git pull        

¿Como trabajar?
    Necestiamos un repo local y uno remoto.
        Desde el local haremos cambios que luego vamos a agregfar al repositorio remoto.
    Primera vez que usas GIT vas a tener que configurar tu nombre completo y tu email con los siguientes comandos
        git config --global user.name "Tu nombre"
        git config --global user.name "Tu direccion de email"
        
Conflictos
    Primera opcion
        git pull antes de realizar algun cambio
    Segunda Opcion
        Se da principalmente cuando se trbaja simultaneamente o cuando se realizo un git pull antes de modificar el archivo

Ramas
    Los comandos mas generales que se usan para trabajar con ramas son:
        git branch
        git branch nombre
        git branch -d nombre
        git branch -D nombre
        git branch -m nombre2
    La manera de poder moverse entre ramas es con el comando checkout
        git checkout nombre
        git checkout -b nombre
    Unir ramas
        git merge nombre
        

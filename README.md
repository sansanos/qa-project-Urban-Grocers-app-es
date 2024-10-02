
# Proyecto para el séptimo sprint (Urban Grocers app)

Otro QA Engineer que trabaja contigo está comprobando cómo la aplicación Urban Grocers crea kits de productos. 
Se han creado varias listas de comprobación, una de ellas es para el campo name en la solicitud de creación de un kit
de productos.

Tu tarea es automatizar las pruebas desde esta lista de comprobación, cargar el código en GitHub y enviar 
el repositorio a revisión


## Pasos para ejecutar las pruebas
Configuración
Trabajarás con Git y GitHub en este proyecto. Sigue los pasos a continuación para configurar tu proyecto.

Paso 1: conecta tu GitHub
El primer paso es enlazar tu cuenta de GitHub a TripleTen. Para ello, haz clic en el botón "Enlazar la cuenta de 
GitHub" en el widget en la parte superior de esta página. Esto te llevará a una nueva pestaña del navegador 
donde se te pedirá que confirmes que deseas enlazar tu cuenta de GitHub. Si aún no has iniciado sesión en GitHub, 
se te pedirá que introduzcas tu nombre de usuario y contraseña. Al confirmarlo, tu perfil de TripleTen se 
conectará a tu perfil de GitHub a través de la API segura de GitHub. Esto te permitirá enviar tus proyectos 
automáticamente con tan solo hacer clic en un botón, directamente dentro de la plataforma de TripleTen.

Paso 2. Clona el repositorio en tu computadora
Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. 
El nombre del repositorio será qa-project-Urban-Grocers-app-es.

Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:

1. Abre la línea de comandos en tu computadora.
2. Si aún no lo has hecho, crea un directorio para almacenar todos tus proyectos. 
3. Clona el repositorio con SSH.

Paso 3. Trabaja con el proyecto de forma local
Ahora tienes una copia local del proyecto y puedes abrir la carpeta del proyecto en tu computadora.

Presiona el botón "Iniciar el servidor" para obtener la URL de tu servidor.

Abre la documentación para estudiar la API de la aplicación de Urban Grocers: 
<the url of the launched server>/docs/.

Busca "Main.Kits" →" Crear un kit.”

Creación de un kit para el usuario o usuaria

Vas a crear un kit dentro de un usuario o usuaria particular, no una tarjeta. Para ello, sigue estos pasos:

Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también 
el encabezado Autorization.
Después de eso, simplemente utiliza la lista de comprobación. Los resultados de la prueba serán diferentes cada vez, 
según el cuerpo de solicitud. Sin embargo, los pasos serán los mismos.

Lista de comprobación de pruebas

1	El número permitido de caracteres (1): 
kit_body = { "name": "a"}	
Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la 
solicitud

2	El número permitido de caracteres (511): 
kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}	
Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo 
de la solicitud

3	El número de caracteres es menor que la cantidad permitida (0): 
kit_body = { "name": "" }	Código de respuesta: 400

4	El número de caracteres es mayor que la cantidad permitida (512): 
kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	Código de respuesta: 400
5	Se permiten caracteres especiales: kit_body = 
{ "name": ""№%@"," }	
Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la 
solicitud

6	Se permiten espacios: kit_body = 
{ "name": " A Aaa " }	
Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la 
solicitud

7	Se permiten números: kit_body = 
{ "name": "123" }	
Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la 
solicitud

8	El parámetro no se pasa en la solicitud: kit_body = { }	Código de respuesta: 400

9	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	Código de respuesta: 400
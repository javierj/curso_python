 Ejercicios del curso Python y Pruebas
=========================================================

Módulo 05: Pruebas en Entornos Específicos

Modificación del ejemplo que hicimos en el módulo 3 y que se conecta a un servicio web para traer información de una película, siempre que dicha película no esté guardada en una caché. Los cambios son:

1) Añadir una caché que funciona con MongoDB además de la caché con SQLite3.

2) Nuevas pruebas que verifican el uso de la caché con la librería MongoMock. Estas pruebas se pueden ejecutar sin un servidor de MongoDB.

3) Nuevas pruebas que interceptan la llamada a la API Rest para devolver un valor concreto. Además, se usa MonkeyPatch para verificar que el código de producción muestra la película correcta.






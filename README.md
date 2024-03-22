# reto_final
1. Instalar todas las dependencias en el archivo requirements.txt
pip install -r requirements.txt

2. Usar manage.sh para crear la base de datos si no está creada

3. Ejecutar run.py para iniciar la app
python run.py

4. Para ver la base de datos
http://tu-localhost:puerto/data

5. Agregar un dato a la base de datos realizando una solicitud POST a la ruta "/data" con los datos que deseas agregar
curl -X POST -H "Content-Type: application/json" -d '{"name": "NuevoDato"}' http://tu-localhost:puerto/data

6. Consultar la base de datos utilizando la solicitud GET a la ruta "/data"
curl http://tu-localhost:puerto/data

7. Eliminar un dato de la base de datos utilizando la solicitud DELETE a la ruta /data/<id>
curl -X DELETE http://tu-localhost:puerto/data/ID_A_ELIMINAR

8. Para probar los tests
python -m unittest tests/test_database.py

9. Para ver la cobertura
coverage run --source=app -m unittest discover -s tests
coverage report -m



Creación de Pipeline de CI

1. Jenkins:
- Crear un nuevo Pipeline.
- En "Build Triggers" marcar la casilla "GitHub hook trigger for GITScm polling"
- En la sección "Pipeline":
    - Seleccionar "Pipeline script from SCM" y seleccione "Git" como SCM.
    - Ingresar la URL del repositorio y configure las credenciales. (Si es público el repositorio no hace falta declarar credenciales)
    - En "Branches to build" poner "*/main"
    - En "Script Path" poner la ruta hacia Jenkinsfile.
    - Guardar configuración.

2. Ngrok (Windows):
- Crear cuenta o iniciar sesión en ngrok
- Instalar ngrok
- Ejecutar el siguiente comando para agregar el authtoken al ngrok.yml
  ngrok config add-authtoken "tu_Authtoken"
- Desplegrar ngrok:
  ngrok http http://localhost:8080
- Copiar la URL pública generada.

3. GitHub
- Crear un nuevo Webhook en el repositorio de GitHub
- Poner la URL de ngrok en "Payload URL" seguido de "github-webhook/":
  Ejemplo: https://0f3f-188-78-186-22.ngrok-free.app/github-webhook/
- En "Content type" seleccionar la opción "aplication/json"
- En "Which events would you like to trigger this webhook?" seleccionar "Just the push event"
- Guardar el Webhook.

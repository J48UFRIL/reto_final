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

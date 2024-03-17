import unittest
from flask_testing import TestCase
from app import create_app, db
from app.models import Data


class TestDatabaseOperations(TestCase):

    def create_app(self):
        app = create_app("test")
        return app

    # Crear base de datos
    def setUp(self):
        with self.app.app_context():
            db.create_all()

    # Eliminar base de datos
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    # Realizar pruebas de inserción de datos en la base de datos
    def test_insert_data(self):
        print("\nTest Insertar Datos:")
        with self.app.app_context():
            new_data = Data(name="TestDato")
            db.session.add(new_data)
            db.session.commit()

            # Verificar que el dato fue insertado correctamente
            data_in_db = Data.query.filter_by(name='TestDato').first()
            print(f"Se ha añadido el siguiente dato: {data_in_db}")
            self.assertIsNotNone(data_in_db)
            self.assertEqual(data_in_db.name, 'TestDato')

    # Realizar pruebas de consulta de datos en la base de datos
    def test_query_data(self):
        print("\n\nTest consultar datos:")
        with self.app.app_context():
            # Insertar datos de prueba
            db.session.add(Data(name='Dato1'))
            db.session.add(Data(name='Dato2'))
            db.session.commit()

            # Realizar una solicitud GET a la ruta /data
            response = self.client.get('/data')
            data_list = response.get_json()
            print(f"Consulta de datos: {data_list}")

            # Verificar que se obtengan los datos correctamente
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data_list), 2)
            self.assertEqual(data_list[0]['name'], 'Dato1')
            self.assertEqual(data_list[1]['name'], 'Dato2')

    # Realizar pruebas de eliminación de datos en la base de datos
    def test_delete_data(self):
        with self.app.app_context():
            # Insertar un dato de prueba
            db.session.add(Data(name='DatoEliminar'))
            db.session.commit()

            # Realizar una solicitud DELETE para eliminar el dato
            # Asumiendo que el ID del dato es 1
            response = self.client.delete('/data/1')
            deleted_data = Data.query.get(1)

            # Verificar que el dato fue eliminado correctamente
            self.assertEqual(response.status_code, 200)
            self.assertIsNone(deleted_data)


if __name__ == '__main__':
    unittest.main()

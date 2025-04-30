import psycopg2


conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try:
    with conexion as conexion:
        with conexion.cursor() as cursor:
            
            # Eliminar un registro
            sql = 'DELETE FROM usuarios WHERE id_usuario >= %s'
            id = (4,) # Tupla con un solo elemento
            
            cursor.execute(sql, id)
            
            registros_eliminados = cursor.rowcount
            print(f'Se han eliminado {registros_eliminados} registros')
            
            
except Exception as ex:
    print("Error:", ex)
finally:
    conexion.close()
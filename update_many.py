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
            
            # Actualizar un registro
            sql = 'UPDATE usuarios SET nombre = %s WHERE id_usuario = %s'
            valores = (('Patata', 3), ('Tontin',5), ('Pocholo', 6))
            
            cursor.executemany(sql, valores)
            
            registros_updateados = cursor.rowcount
            print(f'Se han updateado {registros_updateados} registros')
            
            
except Exception as ex:
    print("Error:", ex)
finally:
    conexion.close()
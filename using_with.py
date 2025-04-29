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
            
            query = 'SELECT * FROM usuarios'
            cursor.execute(query)
            registros = cursor.fetchall()
            #Muestro los datos devueltos por la consulta
            print(registros)
except Exception as ex:
    print("Error:", ex)
finally:
    conexion.close()
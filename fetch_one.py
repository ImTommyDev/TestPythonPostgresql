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
            
            query = 'SELECT id_usuario,nombre,edad FROM usuarios WHERE id_usuario = %s'
            id_usuario = input("Introduce el id del usuario: ")
            cursor.execute(query, (id_usuario,)) #le pongo una , al final porque le tengo que pasar una tupla, si no le pongo la , me da error
            registros = cursor.fetchone() #Como solo estoy recuperando un registro, puedo usar fetchone, de esta manera es más eficiente que usar fetchall
            #Muestro los datos devueltos por la consulta
            print(registros)
except Exception as ex:
    print("Error:", ex)
finally:
    conexion.close()
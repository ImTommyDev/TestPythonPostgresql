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
            
            query = 'SELECT id_usuario,nombre,edad FROM usuarios WHERE id_usuario IN %s'
            # claves_primarias = ((1,2,3),) #Tengo que pasarle una tupla de tuplas para que funcione el IN
            
            entrada = input('Ingrese los id de los usuarios separados por comas: ')
            claves_primarias = (tuple(entrada.split(',')),)
            
            cursor.execute(query, claves_primarias)
            registros = cursor.fetchall()
            #Muestro los datos devueltos por la consulta
            for registro in registros:
                print(f'ID: {registro[0]} Nombre: {registro[1]} Edad: {registro[2]}')
except Exception as ex:
    print("Error:", ex)
finally:
    conexion.close()
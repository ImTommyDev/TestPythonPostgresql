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
            
            sentencia = 'INSERT INTO usuarios (nombre, edad, email) VALUES (%s, %s, %s)'
            valores = ('Lucas',30,'llucas@gmail.com')
            cursor.execute(sentencia, valores)
            
            # No hace falta que haga commit (para guardar los datos), ya que estoy usando el with
            
            registros_insertados = cursor.rowcount
            print(f'Se han insertado {registros_insertados} registros')
            
            
except Exception as ex:
    print("Error:", ex)
finally:
    conexion.close()
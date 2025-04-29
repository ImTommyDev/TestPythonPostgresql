import psycopg2


conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# print("Conexion exitosa:", conexion)

#El cursor es para ejecutar sentencias SQL
cursor = conexion.cursor()

query = 'SELECT * FROM usuarios'
cursor.execute(query)
registros = cursor.fetchall()
#Muestro los datos devueltos por la consulta
print("Total de registros:", len(registros))
for registro in registros:
    print(registro)

cursor.close()
conexion.close()
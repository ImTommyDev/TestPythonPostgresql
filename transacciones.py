import psycopg2 as bd


conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)


#IMPORTANTE: Se puede hacer asi o con el with como hemos hecho anteriormente en el ejemplo insert_many
try:
    #Creo una transacción
    conexion.autocommit = False # Hasta que no se haga un commit, no se guardan los cambios en la base de datos
    
    cursor = conexion.cursor()
    
    sentencia = 'INSERT INTO usuarios (nombre, edad, email) VALUES (%s, %s, %s)'
    valores = (('Mario',20,'mmario@gmail.com')
                ,('Juan',25,'jjuan@gmail.com')
                , ('Pedro',35,'ppedro@gmail.com'))
    cursor.executemany(sentencia, valores)
    
    sentencia = 'UPDATE usuarios SET edad = %s WHERE id_usuario = %s'
    valores = ((40, 12))
    cursor.execute(sentencia, valores)
    
    # Si no hay errores, se hace el commit
    conexion.commit()
    
except Exception as ex:
    #Si hay un error, se hace un rollback
    conexion.rollback()
    print(f"Error en la transacción, se hace un rollback {ex}")
finally:
    conexion.close()
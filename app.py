import mysql.connector

def conectar_db():
    conexion = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        port = 3306,
        database = 'persona'
    )
    return conexion

def crear_persona(nombre,edad):
    conexion = conectar_db()
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO tabla_persona (nombre,edad) VALUES ('" + nombre + "'," + str(edad) + ");"
       # sql = "INSERT INTO `persona`.`tabla_persona`(`nombre`,`edad`) VALUES ('"+nombre+"',"+str(edad)+");"

        cursor.execute(sql)
        conexion.commit()
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__)
    finally:
        conexion.close()  # Cerramos la conexion a la BD

def borrar_persona(id):
    conexion = conectar_db()
    try:
        cursor=conexion.cursor()
        sql = f"DELETE FROM tabla_persona WHERE id={id};"
        cursor.execute(sql)
        conexion.commit()

    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__)
    finally:
        conexion.close()  # Cerramos la conexion a la BD

def modificar_persona(nombre,edad,id):
    conexion=conectar_db()
    try:
        cursor=conexion.cursor()

        sql = f"UPDATE tabla_persona SET nombre='{nombre}',edad={edad} WHERE id={id};"

        cursor.execute(sql)
        conexion.commit()
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__)
    finally:
        print("Conexion cerrada")
        conexion.close()  # Cerramos la conexion a la BD

def leer_persona():
    conexion=conectar_db()
    try:
        cursor=conexion.cursor()
        sql = "select * from tabla_persona;"
        cursor.execute(sql)
        listado_personas = cursor.fetchall()
        return listado_personas
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__)
    finally:
        print("Conexion cerrada")
        conexion.close()  # Cerramos la conexion a la BD

""" nombre=input("Ingrese nombre: ")
edad=int(input("ingrese edad: "))

crear_persona(nombre,edad) """

'''
id=int(input("Ingrese id para eliminar: "))
borrar_persona(id)
'''

'''
nombre=input("Ingrese nombre: ")
edad = int(input("ingrese edad: "))
id = int(input("Ingrese id a modificar: "))

modificar_persona(nombre,edad,id)
'''

persona = leer_persona()
for i in persona:
    print(i)




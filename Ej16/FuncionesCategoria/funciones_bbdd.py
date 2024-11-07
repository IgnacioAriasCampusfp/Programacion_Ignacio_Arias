import mysql.connector

def conectar(baseDatos):
    
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        #password="curso",
        database=baseDatos   
    )

    return conexion





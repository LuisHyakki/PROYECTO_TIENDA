import sqlite3
import os
import sys

def consulta_sql(sql_query, parametros=None):
    cursor = conexion.cursor()
    if parametros:
        cursor.execute(sql_query, parametros)
    else:
        cursor.execute(sql_query)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


def cambio_sql(sql_query, parametros=None):
    cursor = conexion.cursor()
    try:
        if parametros:
            cursor.execute(sql_query, parametros)
        else:
            cursor.execute(sql_query)
        conexion.commit()
        print("Operación realizada con éxito.")
    except Exception as e:
        print(f"Error al ejecutar modificación: {e}")
        conexion.rollback()
    finally:
        cursor.close()

def obtener_ruta_recurso(ruta_relativa):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, ruta_relativa)

ruta_db = obtener_ruta_recurso("utils/base_de_datos.db")
conexion = sqlite3.connect(ruta_db)
conexion.row_factory = sqlite3.Row

#icono
ruta_icono = obtener_ruta_recurso("assets/icono_main.ico")

import psycopg2

def connect():
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname="registros",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    return conn

def consultar_registros():
    conn = connect()
    registros = []
    try:
        cursor = conn.cursor()
        query = """
                    SELECT * 
                    FROM registro;
                    """
        cursor.execute(query)
        registros = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener los registros {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    print(registros)
    return registros


def buscar_usuario(usuario):
    conn = connect()
    registro = []
    try:
        cursor = conn.cursor()
        query = """SELECT email, password FROM registro WHERE email = %s;"""
        cursor.execute(query, (usuario,))
        registro = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener el usuario: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

    print(registro)
    return registro

def insertar_registro(nombre, apellidos, email, password, fecha_nacimiento):
    conn = connect()

    try:
        cursor = conn.cursor()
        query = """
                INSERT INTO registro (nombre, apellidos, email, password, fecha_nacimiento)
                VALUES (%s, %s, %s, %s, %s);
                """
        cursor.execute(query, (nombre, apellidos, email, password, fecha_nacimiento))
        conn.commit()
        print("Registro guardado")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

    consultar_registros()
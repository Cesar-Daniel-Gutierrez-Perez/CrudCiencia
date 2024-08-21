import mysql.connector
from mysql.connector import Error

# Configuración de la conexión
config = {
    'user': 'studentsucundi',
    'password': 'mami_prende_la_radi0',
    'host': '18.116.82.240',
    'port': '3306',
    'database': 'employees'
}

try:
    # Establecer la conexión
    conexion = mysql.connector.connect(**config)
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos")

        # Crear un cursor para realizar operaciones
        cursor = conexion.cursor()

        # Crear una tabla
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            puesto VARCHAR(255) NOT NULL,
            salario DECIMAL(10, 2) NOT NULL
        )
        """)
        print("Tabla creada")

        # Insertar datos en la tabla
        cursor.execute("""
        INSERT INTO empleados (nombre, puesto, salario)
        VALUES ('Juan Pérez', 'Desarrollador', 50000.00)
        """)
        conexion.commit()
        print("Datos insertados")

        # Consultar datos de la tabla
        cursor.execute("SELECT * FROM empleados")
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)

except Error as err:
    # Si no se establece la conexión
    print(f"Error: {err}")

finally:
    # Cerrar la conexion
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada")
from faker import Faker
import mysql.connector
import random

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="Usuario",
    password="Contraseña",
    database="nodoITST"
)

cursor = db.cursor()

# Instancia de Faker
fake = Faker('es_MX')

# Obtener EMPLEADO existentes
cursor.execute("SELECT ID_Empleado FROM EMPLEADO")
empleado_ids = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla ADMINISTRATIVO
for _ in range(30):  # Cambia 10 por el número de registros que desees crear
    
    id_empleado = random.choice(empleado_ids)
    area = random.choice(['Académico', 'Administrativo', 'Becas','Extra Escolares'])
    cargo = fake.job()
    descripcion_puesto = fake.text()

    # Insertar datos en la tabla ADMINISTRATIVO
    cursor.execute("INSERT INTO ADMINISTRATIVO (ID_Empleado, Area, Cargo, DescripcionPuesto) VALUES (%s, %s, %s, %s)",
                   (id_empleado, area, cargo, descripcion_puesto))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

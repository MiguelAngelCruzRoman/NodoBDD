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

# Obtener IDs de plataforma existentes
cursor.execute("SELECT ID_Plataforma FROM PLATAFORMA")
plataforma_ids = [row[0] for row in cursor.fetchall()]

# Obtener IDs de empleado existentes
cursor.execute("SELECT ID_Empleado FROM EMPLEADO")
empleado_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla PLATAFORMA_EMPLEADO
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    id_plataforma = random.choice(plataforma_ids)  # Seleccionar un ID de plataforma aleatorio
    id_empleado = random.choice(empleado_ids)  # Seleccionar un ID de empleado aleatorio
    nombre_usuario = fake.user_name()  # Generar un nombre de usuario aleatorio
    contrasenia = fake.password(length=10)  # Generar una contraseña aleatoria

    # Insertar datos en la tabla PLATAFORMA_EMPLEADO
    cursor.execute("INSERT INTO PLATAFORMA_EMPLEADO (ID_Plataforma, ID_Empleado, NombreUsuario, Contrasenia) VALUES (%s, %s, %s, %s)",
                   (id_plataforma, id_empleado, nombre_usuario, contrasenia))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

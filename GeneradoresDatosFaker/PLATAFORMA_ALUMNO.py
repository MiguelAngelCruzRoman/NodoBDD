from faker import Faker
import mysql.connector
import random

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="MeteUnUser",
    password="TamborLaContra",
    database="nodoITST"
)

cursor = db.cursor()

# Instancia de Faker
fake = Faker('es_MX')

# Obtener números de control de alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
numeros_control_alumnos = [row[0] for row in cursor.fetchall()]

# Obtener IDs de plataforma existentes
cursor.execute("SELECT ID_Plataforma FROM PLATAFORMA")
plataforma_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla PLATAFORMA_ALUMNO
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    no_control_alumno = random.choice(numeros_control_alumnos)  # Seleccionar un número de control de alumno aleatorio
    id_plataforma = random.choice(plataforma_ids)  # Seleccionar un ID de plataforma aleatorio
    nombre_usuario = fake.user_name()  # Generar un nombre de usuario aleatorio
    contrasenia = fake.password(length=10)  # Generar una contraseña aleatoria

    # Insertar datos en la tabla PLATAFORMA_ALUMNO
    cursor.execute("INSERT INTO PLATAFORMA_ALUMNO (NoControl_Alumno, ID_Plataforma, NombreUsuario, Contrasenia) VALUES (%s, %s, %s, %s)",
                   (no_control_alumno, id_plataforma, nombre_usuario, contrasenia))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

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

# Obtener IDs de empleados existentes
cursor.execute("SELECT ID_Empleado FROM EMPLEADO")
empleados_ids = [row[0] for row in cursor.fetchall()]

# Obtener IDs de edificios existentes
cursor.execute("SELECT ID_Edificio FROM EDIFICIO")
edificios_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla DEPARTAMENTO
for _ in range(20):  # Cambia 10 por el número de registros que desees crear
    nombre_departamento = fake.company()  # Generar nombre de departamento aleatorio
    finalidad = fake.text(max_nb_chars=200)  # Generar finalidad aleatoria
    id_empleado_responsable = random.choice(empleados_ids)  # Seleccionar un empleado responsable aleatorio
    id_edificio = random.choice(edificios_ids)  # Seleccionar un edificio aleatorio

    # Insertar datos en la tabla DEPARTAMENTO
    cursor.execute("INSERT INTO DEPARTAMENTO (Nombre, Finalidad, ID_Empleado_Responsable, ID_Edificio) VALUES (%s, %s, %s, %s)",
                   (nombre_departamento, finalidad, id_empleado_responsable, id_edificio))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

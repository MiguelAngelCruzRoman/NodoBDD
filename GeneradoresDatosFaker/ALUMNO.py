from faker import Faker
import mysql.connector
import random
from datetime import datetime, timedelta

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

# Obtener IDs de Estatus existentes
cursor.execute("SELECT ID_Estatus FROM ESTATUS")
estatus_ids = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla ALUMNO
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    # Generar dos dígitos numéricos aleatorios
    digits = ''.join([str(random.randint(0, 9)) for _ in range(2)])

    # Generar cuatro dígitos numéricos aleatorios
    numbers = ''.join([str(random.randint(0, 9)) for _ in range(4)])

    # Generar dos letras aleatorias
    letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
    no_control = digits + letters + numbers

    primer_nombre = fake.first_name()
    segundo_nombre = fake.first_name() if random.random() > 0.5 else None
    apellido_paterno = fake.last_name()
    apellido_materno = fake.last_name()
    fotografia = bytes([random.randint(0, 255) for _ in range(1024)]) 
    semestre = fake.random_int(1, 12)

    # Generar datod curp
    digits = ''.join([str(random.randint(0, 9)) for _ in range(2)])
    numbers = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
    letter = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6))
    curp = letters+numbers+letter+digits

    nss = fake.unique.random_number(digits=10)
    correo_institucional = fake.email()
    correo_personal = fake.email()
    numero_contacto = fake.random_number(digits=10)
    creditos_aprobados = fake.random_int(0, 200)
    fecha_ingreso = fake.date_between(start_date='-30y', end_date='today')
    fecha_egreso = fake.date_between(start_date=fecha_ingreso, end_date='today') if random.random() > 0.5 else None
    id_estatus = random.choice(estatus_ids)

    # Insertar datos en la tabla ALUMNO
    cursor.execute("INSERT INTO ALUMNO (NoControl, PrimerNombre, SegundoNombre, ApellidoPaterno, ApellidoMaterno, Fotografia, Semestre, CURP, NSS, CorreoInstitucional, CorreoPersonal, NumeroContacto, CreditosAprobados, FechaIngreso, FechaEgreso, ID_Estatus_Estatus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (no_control, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, fotografia, semestre, curp, nss, correo_institucional, correo_personal, numero_contacto, creditos_aprobados, fecha_ingreso, fecha_egreso, id_estatus))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

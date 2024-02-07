from faker import Faker
import mysql.connector
import random
from datetime import datetime, timedelta

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

# Generar datos falsos y agregarlos a la tabla EMPLEADO
for _ in range(200):  # Cambia 10 por el número de registros que desees crear
    primer_nombre = fake.first_name()
    segundo_nombre = fake.first_name() if random.random() > 0.5 else None
    apellido_paterno = fake.last_name()
    apellido_materno = fake.last_name()
    
    # Generar datod curp
    digits = ''.join([str(random.randint(0, 9)) for _ in range(2)])
    numbers = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
    letter = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6))
    curp = letters+numbers+letter+digits

    nss = fake.unique.random_number(digits=10)
    antiguedad = fake.random_int(0, 40)
    division = random.choice(['Informática', 'Sistemas', 'Gestión','Turismo','Industrial','Artes Digitales']) if random.random() > 0.5 else None
    ocupacion = random.choice(['Tutor', 'Limpieza', 'Cocinero','oficinista']) if random.random() > 0.5 else None
    grado_escolar = fake.random_element(elements=("Primaria", "Secundaria", "Preparatoria", "Licenciatura", "Maestría", "Doctorado"))
    fecha_contratacion = fake.date_between(start_date='-30y', end_date='-1d')
    dias_vacaciones = fake.random_int(5, 30)
    fecha_jubilacion = fake.date_between(start_date=fecha_contratacion + timedelta(days=365*20), end_date=fecha_contratacion + timedelta(days=365*40)) if antiguedad >= 20 else None

    # Insertar datos en la tabla EMPLEADO
    cursor.execute("INSERT INTO EMPLEADO (PrimerNombre, SegundoNombre, ApellidoPaterno, ApellidoMaterno, CURP, NSS, Antiguedad, Division, Ocupacion, GradoEscolar, FechaContratacion, DiasVacaciones, Fecha_Jubilacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, curp, nss, antiguedad, division, ocupacion, grado_escolar, fecha_contratacion, dias_vacaciones, fecha_jubilacion))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

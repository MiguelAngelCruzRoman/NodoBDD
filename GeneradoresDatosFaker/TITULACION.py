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

# Obtener números de control de Alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
nocontrol_alumnos = [row[0] for row in cursor.fetchall()]

# Obtener IDs de Docente existentes
cursor.execute("SELECT ID_Empleado FROM DOCENTE")
docente_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla TITULACION
for _ in range(50):  # Cambia 10 por el número de registros que desees crear
    nocontrol_alumno = random.choice(nocontrol_alumnos)
    asesor = random.choice(docente_ids)
    grado = fake.random_element(elements=("Licenciatura", "Maestria", "Doctorado"))
    area = fake.job()
    fecha_titulacion = fake.date_between(start_date='-20y', end_date='today')
    division = random.choice(['Informática', 'Sistemas', 'Gestión','Industrial','Turismo'])
    objetivo = fake.sentence(nb_words=8, variable_nb_words=True, ext_word_list=None)
    calificacion = round(random.uniform(6, 10), 2)  # Calificación aleatoria entre 6 y 10

    # Insertar datos en la tabla TITULACION
    cursor.execute("INSERT INTO TITULACION (NoControl_Alumno, Asesor, Grado, Area, FechaTitulacion, Division, Objetivo, Calificacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (nocontrol_alumno, asesor, grado, area, fecha_titulacion, division, objetivo, calificacion))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

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

# Obtener IDs de Empleado existentes
cursor.execute("SELECT ID_Empleado FROM EMPLEADO")
empleado_ids = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla CONVENIO
for _ in range(50):  # Cambia 10 por el número de registros que desees crear
    representante = random.choice(empleado_ids)
    objetivo = fake.sentence(nb_words=8, variable_nb_words=True, ext_word_list=None)
    descripcion = fake.text()
    fecha_publicacion = fake.date_between(start_date='-20y', end_date='today')
    fecha_inicio = fake.date_between(start_date=fecha_publicacion, end_date='+1y')
    fecha_fin = fake.date_between(start_date=fecha_inicio, end_date='+5y')
    participantes = fake.text()

    # Insertar datos en la tabla CONVENIO
    cursor.execute("INSERT INTO CONVENIO (Representante, Objetivo, Descripcion, FechaPublicacion, FechaInicio, FechaFin, Participantes) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (representante, objetivo, descripcion, fecha_publicacion, fecha_inicio, fecha_fin, participantes))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

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

# Obtener IDs de Titulación existentes
cursor.execute("SELECT ID_Titulacion FROM TITULACION")
titulacion_ids = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla TESIS
for _ in range(40):  # Cambia 10 por el número de registros que desees crear
    titulo = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    resumen = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
    fecha_publicacion = fake.date_between(start_date='-20y', end_date='today')
    colaborador = fake.name() if random.random() > 0.5 else None
    id_titulacion = random.choice(titulacion_ids)

    # Insertar datos en la tabla TESIS
    cursor.execute("INSERT INTO TESIS (Titulo, Resumen, FechaPublicacion, Colaborador, ID_Titulacion) VALUES (%s, %s, %s, %s, %s)",
                   (titulo, resumen, fecha_publicacion, colaborador, id_titulacion))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

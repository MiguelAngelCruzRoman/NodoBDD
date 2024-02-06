from faker import Faker
import mysql.connector
import base64
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

# Obtener claves de plan de estudios existentes
cursor.execute("SELECT Clave FROM PLAN_ESTUDIO")
claves_plan_estudio = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla LICENCIATURA
for _ in range(10):  # Cambia 10 por el número de registros que desees crear
    id_licenciatura = fake.uuid4()[:3]  # Generar ID de licenciatura aleatorio
    nombre = fake.job()  # Generar nombre aleatorio
    duracion = fake.random_int(3, 5)  # Duración aleatoria entre 3 y 5 años
    objetivo_general = fake.paragraph(nb_sentences=3)  # Objetivo general aleatorio
    mision = fake.paragraph(nb_sentences=3)  # Misión aleatoria
    vision = fake.paragraph(nb_sentences=3)  # Visión aleatoria
    perfil_aspirante = fake.paragraph(nb_sentences=3)  # Perfil de aspirante aleatorio
    perfil_egresado = fake.paragraph(nb_sentences=3)  # Perfil de egresado aleatorio
    
    # Logo aleatorio en formato de datos binarios
    ejemplo_texto = fake.text()
    ejemplo_bytes = ejemplo_texto.encode('utf-8')
    logo = base64.b64encode(ejemplo_bytes) 

    clave_plan_estudio = random.choice(claves_plan_estudio) if claves_plan_estudio else None

    # Insertar datos en la tabla LICENCIATURA
    cursor.execute("INSERT INTO LICENCIATURA (ID_Licenciatura, Nombre, Duracion, ObjetivoGeneral, Mision, Vision, PerfilAspirante, PerfilEgresado, Logo, Clave_Plan_Estudios) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (id_licenciatura, nombre, duracion, objetivo_general, mision, vision, perfil_aspirante, perfil_egresado, logo, clave_plan_estudio))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

from faker import Faker
import mysql.connector

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

# Generar datos ficticios y agregarlos a la tabla POSTGRADO
for _ in range(30):  # Cambia 10 por el número de registros que desees crear
    nombre = fake.name()  # Nombre aleatorio
    duracion = fake.random_int(min=3, max=5)  # Duración aleatoria entre 1 y 5
    objetivo_general = fake.paragraph(nb_sentences=3)  # Objetivo general aleatorio
    objetivos_especificos = fake.paragraph(nb_sentences=3)  # Objetivos específicos aleatorios
    linea_investigacion = fake.catch_phrase()  # Línea de investigación aleatoria
    perfil_egreso = fake.paragraph(nb_sentences=3)  # Perfil de egreso aleatorio
    perfil_ingreso = fake.paragraph(nb_sentences=3)  # Perfil de ingreso aleatorio

    # Insertar datos en la tabla POSTGRADO
    cursor.execute("INSERT INTO POSTGRADO (Nombre, Duracion, ObjetivoGeneral, ObjetivosEspecificos, LineaInvestigacion, PerfilEgreso, PerfilIngreso) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (nombre, duracion, objetivo_general, objetivos_especificos, linea_investigacion, perfil_egreso, perfil_ingreso))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

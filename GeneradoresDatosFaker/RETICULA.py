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

# Obtener claves oficiales de materia existentes
cursor.execute("SELECT ClaveOficial FROM MATERIA")
claves_oficiales_materia = [row[0] for row in cursor.fetchall()]

# Obtener claves de plan de estudios existentes
cursor.execute("SELECT Clave FROM PLAN_ESTUDIO")
claves_plan_estudio = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla RETICULA
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    clave = fake.uuid4()[:13]  # Generar clave aleatoria
    clave_oficial_materia = random.choice(claves_oficiales_materia)
    clave_plan_estudio = random.choice(claves_plan_estudio)

    # Insertar datos en la tabla RETICULA
    cursor.execute("INSERT INTO RETICULA (Clave, ClaveOficial_Materia, Clave_Plan_Estudios) VALUES (%s, %s, %s)",
                   (clave, clave_oficial_materia, clave_plan_estudio))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

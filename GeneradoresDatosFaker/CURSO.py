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

# Obtener IDs de ciclo existentes
cursor.execute("SELECT ID_Ciclo FROM CICLO")
ciclo_ids = [row[0] for row in cursor.fetchall()]

# Obtener IDs de licenciatura existentes
cursor.execute("SELECT ID_Licenciatura FROM LICENCIATURA")
licenciatura_ids = [row[0] for row in cursor.fetchall()]

# Obtener claves oficiales de materia existentes
cursor.execute("SELECT ClaveOficial FROM MATERIA")
claves_oficiales_materia = [row[0] for row in cursor.fetchall()]

# Obtener IDs de empleado docente existentes
cursor.execute("SELECT ID_Empleado FROM EMPLEADO")
docente_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla CURSO
for _ in range(200):  # Cambia 10 por el número de registros que desees crear
    clave = fake.uuid4()[:4]  # Generar clave aleatoria
    semestre = fake.random_int(min=1, max=10)  # Semestre aleatorio
    letra_grupo = random.choice(["A", "B", "C", "D"])  # Letra de grupo aleatoria
    id_ciclo = random.choice(ciclo_ids)  # ID de ciclo aleatorio
    id_licenciatura = random.choice(licenciatura_ids)  # ID de licenciatura aleatorio
    clave_oficial_materia = random.choice(claves_oficiales_materia)  # Clave oficial de materia aleatoria
    id_empleado_docente = random.choice(docente_ids)  # ID de empleado docente aleatorio

    # Insertar datos en la tabla CURSO
    cursor.execute("INSERT INTO CURSO (Clave, Semestre, LetraGrupo, ID_Ciclo, ID_Licenciatura, ClaveOficial_Materia, ID_Empleado_Docente) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (clave, semestre, letra_grupo, id_ciclo, id_licenciatura, clave_oficial_materia, id_empleado_docente))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

from faker import Faker
import mysql.connector

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

# Generar datos ficticios y agregarlos a la tabla MATERIA
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    clave_oficial = fake.uuid4()[:8]  # Generar clave oficial aleatoria
    nombre = fake.catch_phrase()  # Generar nombre aleatorio
    unidades = fake.random_int(min=1, max=10)  # Unidades aleatorias
    creditos = fake.random_int(min=1, max=10)  # Créditos aleatorios
    horas_practicas = fake.random_int(min=1, max=creditos)  # Horas prácticas aleatorias
    horas_teoricas = creditos-horas_practicas  # Horas teóricas aleatorias

    # Insertar datos en la tabla MATERIA
    cursor.execute("INSERT INTO MATERIA (ClaveOficial, Nombre, Unidades, Creditos, HorasPracticas, HorasTeoricas) VALUES (%s, %s, %s, %s, %s, %s)",
                   (clave_oficial, nombre, unidades, creditos, horas_practicas, horas_teoricas))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

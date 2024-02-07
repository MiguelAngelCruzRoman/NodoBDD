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

# Generar datos ficticios y agregarlos a la tabla MOBILIARIO
for _ in range(200):  # Cambia 10 por el número de registros que desees crear
    tipo = fake.random_element(elements=('Silla', 'Mesa', 'Escritorio', 'Armario', 'Estante','Proyector','Computadora'))  # Tipo de mobiliario aleatorio
    estado = fake.random_element(elements=('Nuevo', 'Usado', 'Reparación'))  # Estado aleatorio
    detalles = fake.text(max_nb_chars=200)  # Detalles aleatorios

    # Insertar datos en la tabla MOBILIARIO
    cursor.execute("INSERT INTO MOBILIARIO (Tipo, Estado, Detalles) VALUES (%s, %s, %s)",
                   (tipo, estado, detalles))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

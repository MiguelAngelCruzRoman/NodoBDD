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

# Generar datos ficticios y agregarlos a la tabla EDIFICIO
for _ in range(10):  # Cambia 10 por el número de registros que desees crear
    id_edificio = fake.random_uppercase_letter()  # Generar ID de edificio aleatorio
    nombre = fake.company()  # Generar nombre de edificio aleatorio
    fecha_construccion = fake.date_between(start_date='-30y', end_date='today')  # Fecha de construcción aleatoria en los últimos 50 años
    pisos = fake.random_int(min=1, max=3)  # Cantidad de pisos aleatoria entre 1 y 10
    proposito = fake.text(max_nb_chars=100)  # Propósito aleatorio

    # Insertar datos en la tabla EDIFICIO
    cursor.execute("INSERT INTO EDIFICIO (ID_Edificio, Nombre, FechaConstruccion, Pisos, Proposito) VALUES (%s, %s, %s, %s, %s)",
                   (id_edificio, nombre, fecha_construccion, pisos, proposito))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

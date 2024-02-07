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

# Días de la semana disponibles
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']

# Generar datos ficticios y agregarlos a la tabla HORARIO
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    dia_semana = fake.random_element(elements=dias_semana)  # Seleccionar un día de la semana aleatorio
    hora_inicio = fake.time(pattern="%H:%M:%S", end_datetime=None)  # Generar una hora de inicio aleatoria
    hora_final = fake.time(pattern="%H:%M:%S", end_datetime=None)  # Generar una hora de finalización aleatoria

    # Insertar datos en la tabla HORARIO
    cursor.execute("INSERT INTO HORARIO (DiaSemana, HoraInicio, HoraFinal) VALUES (%s, %s, %s)",
                   (dia_semana, hora_inicio, hora_final))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

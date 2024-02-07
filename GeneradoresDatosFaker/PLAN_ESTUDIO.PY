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

# Generar datos ficticios y agregarlos a la tabla PLAN_ESTUDIO
for _ in range(30):  # Cambia 10 por el número de registros que desees crear
    clave = fake.uuid4()[:20]  # Generar clave aleatoria
    especialidad = fake.job()  # Generar especialidad aleatoria
    grupos = fake.random_element(elements=("A", "B", "C", "D"))  # Grupos aleatorios
    sistema = fake.random_element(elements=("Escolarizado", "Mixo", "Virtual"))  # Sistema aleatorio
    fecha_elaboracion = fake.date_between(start_date='-30y', end_date='today')  # Fecha de elaboración aleatoria
    inicio_vigencia = fake.date_between(start_date=fecha_elaboracion, end_date='today')  # Fecha de inicio de vigencia aleatoria
    fin_vigencia = fake.date_between(start_date=inicio_vigencia, end_date='+5y')  # Fecha de fin de vigencia aleatoria

    # Insertar datos en la tabla PLAN_ESTUDIO
    cursor.execute("INSERT INTO PLAN_ESTUDIO (Clave, Especialidad, Grupos, Sistema, InicioVigengia, FinVigencia, FechaElaboracion) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (clave, especialidad, grupos, sistema, inicio_vigencia, fin_vigencia, fecha_elaboracion))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

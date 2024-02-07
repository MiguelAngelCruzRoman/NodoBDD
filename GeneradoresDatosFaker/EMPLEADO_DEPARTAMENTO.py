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

# Obtener IDs de empleados existentes
cursor.execute("SELECT ID_Empleado FROM EMPLEADO")
empleados_ids = [row[0] for row in cursor.fetchall()]

# Obtener IDs de departamentos existentes
cursor.execute("SELECT ID_Departamento FROM DEPARTAMENTO")
departamentos_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla EMPLEADO_DEPARTAMENTO
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    id_empleado = random.choice(empleados_ids)  # Seleccionar un ID de empleado aleatorio
    id_departamento = random.choice(departamentos_ids)  # Seleccionar un ID de departamento aleatorio
    fecha_inicio_labor = fake.date_between(start_date='-30y', end_date='today')  # Fecha de inicio de labor aleatoria en los últimos 5 años
    fecha_fin_labor = fake.date_between(start_date=fecha_inicio_labor, end_date='today') if fake.boolean(chance_of_getting_true=50) else None  # Fecha de fin de labor aleatoria (opcional)

    # Insertar datos en la tabla EMPLEADO_DEPARTAMENTO
    cursor.execute("INSERT INTO EMPLEADO_DEPARTAMENTO (ID_Empleado, ID_Departamento, FechaInicioLabor, FechaFinLabor) VALUES (%s, %s, %s, %s)",
                   (id_empleado, id_departamento, fecha_inicio_labor, fecha_fin_labor))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()

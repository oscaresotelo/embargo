# import sqlite3

# # Crear la conexión a la base de datos o abrir la existente
# conn = sqlite3.connect('embargos.db')
# cursor = conn.cursor()

# # Crear tabla Juicios
# cursor.execute('''CREATE TABLE IF NOT EXISTS Juicios (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     Dni INTEGER,
#                     NombreJuicio TEXT,
#                     NumerodeExpte INTEGER,
#                     RadicacionJudicial INTEGER,
#                     NumeroOficio INTEGER,
#                     NumeroExpteAdministrativo INTEGER,
#                     MedidaCautelar INTEGER,
#                     AclaracionCautelar TEXT,
#                     FechaInicio DATE,
#                     FechaFin DATE,
#                     Observacion TEXT,
#                     MontoEmbargo REAL,
#                     Sanciones INTEGER
#                 )''')

# # Crear tabla Radicacion
# cursor.execute('''CREATE TABLE IF NOT EXISTS Radicacion (
#                     idradicacion INTEGER PRIMARY KEY,
#                     NombreRadicacion TEXT
#                 )''')

# # Crear tabla Medidas
# cursor.execute('''CREATE TABLE IF NOT EXISTS Medidas (
#                     idmedidas INTEGER PRIMARY KEY,
#                     NombreMedida TEXT
#                 )''')

# # Crear tabla Sanciones
# cursor.execute('''CREATE TABLE IF NOT EXISTS Sanciones (
#                     idsanciones INTEGER PRIMARY KEY,
#                     NombreSancion TEXT
#                 )''')

# # Guardar los cambios y cerrar la conexión
# conn.commit()
# conn.close()
# import sqlite3
# import csv

# # Conexión a la base de datos
# conn = sqlite3.connect('embargos.db')
# c = conn.cursor()

# # Creación de la tabla Radicacion si no existe
# c.execute('''CREATE TABLE IF NOT EXISTS Radicacion 
#              (Juzgado INTEGER, NombreRadicacion TEXT)''')

# # Lectura del archivo CSV y carga de los datos en la tabla Radicacion
# with open('juzgadoconcepcion.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     next(reader)  # saltar la primera fila (cabecera)
#     for row in reader:
#         juzgado = int(row[0])
#         radicacion = row[1]
#         c.execute("INSERT INTO Radicacion (Juzgado, NombreRadicacion) VALUES (?, ?)",
#                   (juzgado, radicacion))

# # Guardar los cambios y cerrar la conexión
# conn.commit()
# conn.close()
import sqlite3
from datetime import datetime, timedelta

# Conectarse a la base de datos SQLite
conn = sqlite3.connect('embargos.db')
cursor = conn.cursor()

# Actualizar los campos FechaUltimaNotificacion y FechaProximaNotificacion
cursor.execute('''SELECT id, FechaUltimaNotificacion FROM Juicios''')

# Recorrer los registros y actualizar las fechas
for row in cursor.fetchall():
    id_juicio, fecha_ultima_notif_str = row
    if fecha_ultima_notif_str is not None:
        # Convertir la cadena a un objeto datetime
        fecha_ultima_notif = datetime.strptime(fecha_ultima_notif_str, '%Y-%m-%d')

        # Sumar 30 días a la FechaUltimaNotificacion
        fecha_prox_notif = fecha_ultima_notif + timedelta(days=30)

        # Convertir el resultado de vuelta a una cadena en el formato correcto (YYYY-MM-DD)
        fecha_prox_notif_str = fecha_prox_notif.strftime('%Y-%m-%d')

        # Actualizar el campo FechaProximaNotificacion en la base de datos
        cursor.execute('''UPDATE Juicios SET FechaProximaNotificacion = ? WHERE id = ?''',
                       (fecha_prox_notif_str, id_juicio))

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión con la base de datos
conn.close()

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
import sqlite3
import csv

# Conexión a la base de datos
conn = sqlite3.connect('embargos.db')
c = conn.cursor()

# Creación de la tabla Radicacion si no existe
c.execute('''CREATE TABLE IF NOT EXISTS Radicacion 
             (Juzgado INTEGER, NombreRadicacion TEXT)''')

# Lectura del archivo CSV y carga de los datos en la tabla Radicacion
with open('juzgadoconcepcion.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # saltar la primera fila (cabecera)
    for row in reader:
        juzgado = int(row[0])
        radicacion = row[1]
        c.execute("INSERT INTO Radicacion (Juzgado, NombreRadicacion) VALUES (?, ?)",
                  (juzgado, radicacion))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

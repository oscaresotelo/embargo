import sqlite3

# Crear la conexión a la base de datos o abrir la existente
conn = sqlite3.connect('embargos.db')
cursor = conn.cursor()

# Crear tabla Juicios
cursor.execute('''CREATE TABLE IF NOT EXISTS Juicios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Dni INTEGER,
                    NombreJuicio TEXT,
                    NumerodeExpte INTEGER,
                    RadicacionJudicial INTEGER,
                    NumeroOficio INTEGER,
                    NumeroExpteAdministrativo INTEGER,
                    MedidaCautelar INTEGER,
                    AclaracionCautelar TEXT,
                    FechaInicio DATE,
                    FechaFin DATE,
                    Observacion TEXT,
                    MontoEmbargo REAL,
                    Sanciones INTEGER
                )''')

# Crear tabla Radicacion
cursor.execute('''CREATE TABLE IF NOT EXISTS Radicacion (
                    idradicacion INTEGER PRIMARY KEY,
                    NombreRadicacion TEXT
                )''')

# Crear tabla Medidas
cursor.execute('''CREATE TABLE IF NOT EXISTS Medidas (
                    idmedidas INTEGER PRIMARY KEY,
                    NombreMedida TEXT
                )''')

# Crear tabla Sanciones
cursor.execute('''CREATE TABLE IF NOT EXISTS Sanciones (
                    idsanciones INTEGER PRIMARY KEY,
                    NombreSancion TEXT
                )''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

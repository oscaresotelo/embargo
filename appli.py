
import sqlite3
import streamlit as st

# Conectar a la base de datos SQLite
conn = sqlite3.connect('embargos.db')

# Obtener un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Ejecutar una consulta para obtener los nombres de las columnas de la tabla Juicios
cursor.execute("PRAGMA table_info(Juicios)")
column_info = cursor.fetchall()
column_names = [info[1] for info in column_info]

# Mostrar los nombres de las columnas en Streamlit
st.write("Nombres de las columnas de la tabla Juicios:")
st.write(column_names)

# Cerrar la conexi\u00f3n a la base de datos SQLite
conn.close()

import streamlit as st
import pandas as pd
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('embargos.db')

# Crear tabla Sanciones si no existe
conn.execute('''CREATE TABLE IF NOT EXISTS Sanciones 
                (idsanciones INTEGER PRIMARY KEY,
                 NombreSancion TEXT)''')

# Definir título de la página
st.title("Tipo de Sanciones")

# Crear campos de entrada para idsanciones y NombreSancion
idsanciones = st.number_input("Ingrese el ID de la sanción:", value=0, step=1)
nombre_sancion = st.text_input("Ingrese el nombre de la sanción:")

# Agregar datos a la tabla Sanciones al presionar el botón "Guardar"
if st.button("Guardar"):
    conn.execute(f"INSERT INTO Sanciones (idsanciones, NombreSancion) VALUES ({idsanciones}, '{nombre_sancion}')")
    conn.commit()
    st.success("Los datos se han guardado correctamente.")

# Leer datos de la tabla Sanciones y mostrarlos debajo del formulario de ingreso
st.subheader("Sanciones existentes:")
df = pd.read_sql_query("SELECT * FROM Sanciones", conn)
st.dataframe(df)

# Cerrar conexión a la base de datos
conn.close()

import sqlite3
import streamlit as st
import pandas as pd

# Conectarse a la base de datos
conn = sqlite3.connect('embargos.db')
c = conn.cursor()

# Crear tabla Medidas si no existe
c.execute('''CREATE TABLE IF NOT EXISTS Medidas
             (idmedida INTEGER PRIMARY KEY, NombreMedida TEXT)''')
             
# Título de la aplicación
st.title("Tipo de Medidas")

# Ingreso de datos
id_medida = st.number_input("Ingrese el ID de la medida:", value=0, step=1)
nombre_medida = st.text_input("Ingrese el nombre de la medida:")

# Botón para guardar los datos
if st.button("Guardar"):
    # Insertar los datos en la tabla Medidas
    c.execute("INSERT INTO Medidas (idmedidas, NombreMedida) VALUES (?, ?)", (id_medida, nombre_medida))
    conn.commit()
    st.success("Los datos han sido guardados correctamente.")

# Mostrar los datos existentes en un dataframe
st.write("Datos existentes en la tabla Medidas:")
df = pd.read_sql_query("SELECT * from Medidas", conn)
st.write(df)

# Cerrar la conexión con la base de datos
conn.close()

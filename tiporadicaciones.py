
# import streamlit as st
# import sqlite3
# import pandas as pd

# conn = sqlite3.connect('embargos.db')
# c = conn.cursor()

# st.title("Tipo de Radicacion")

# id_radicacion = st.number_input("Ingrese el id de la radicación", min_value=0)
# nombre_radicacion = st.text_input("Ingrese el nombre de la radicación")
# juzgado = st.number_input("Localidad", min_value=0)
# # Mostrar los datos existentes
# c.execute("SELECT * FROM Radicacion")
# data = c.fetchall()
# df = pd.DataFrame(data, columns=['ID', 'Juzgado','Radicacion'])
# existing_data_placeholder = st.empty()

# if st.button("Guardar"):
#     c.execute("INSERT INTO Radicacion (idradicacion, Juzgado, NombreRadicacion) VALUES (?, ?, ?)", (id_radicacion, juzgado, nombre_radicacion))
#     conn.commit()

#     # Mostrar los datos existentes actualizados
#     c.execute("SELECT * FROM Radicacion")
#     data = c.fetchall()
#     df = pd.DataFrame(data, columns=['ID', 'Juzgado','Nombre'])
#     existing_data_placeholder.write("Datos existentes:")
#     existing_data_placeholder.write(df)

# # Mostrar los datos existentes
# existing_data_placeholder.write("Datos existentes:")
# existing_data_placeholder.write(df)
import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('embargos.db')
c = conn.cursor()

st.title("Tipo de Radicacion")

id_radicacion = st.number_input("Ingrese el id de la radicación", min_value=0)
nombre_radicacion = st.text_input("Ingrese el nombre de la radicación")

# Obtener los datos de la tabla Juzgados
c.execute("SELECT Localidad FROM Juzgados")
juzgados_data = c.fetchall()
juzgados_options = [row[0] for row in juzgados_data]

# Crear el select_box para elegir la localidad
juzgado = st.selectbox("Localidad", juzgados_options)

# Mostrar los datos existentes
c.execute("SELECT * FROM Radicacion")
data = c.fetchall()
df = pd.DataFrame(data, columns=['ID', 'Juzgado', 'Radicacion'])
existing_data_placeholder = st.empty()

if st.button("Guardar"):
    c.execute("INSERT INTO Radicacion (idradicacion, Juzgado, NombreRadicacion) VALUES (?, ?, ?)",
              (id_radicacion, juzgado, nombre_radicacion))
    conn.commit()

    # Mostrar los datos existentes actualizados
    c.execute("SELECT * FROM Radicacion")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['ID', 'Juzgado', 'Nombre'])
    existing_data_placeholder.write("Datos existentes:")
    existing_data_placeholder.write(df)

# Mostrar los datos existentes
existing_data_placeholder.write("Datos existentes:")
existing_data_placeholder.write(df)

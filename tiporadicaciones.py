# import streamlit as st
# import sqlite3
# import pandas as pd

# conn = sqlite3.connect('embargos.db')
# c = conn.cursor()

# st.title("Tipo de Radicacion")

# id_radicacion = st.number_input("Ingrese el id de la radicación", min_value=0)
# nombre_radicacion = st.text_input("Ingrese el nombre de la radicación")

# if st.button("Guardar"):
#     c.execute("INSERT INTO Radicacion (idradicacion, NombreRadicacion) VALUES (?, ?)", (id_radicacion, nombre_radicacion))
#     conn.commit()

#     # Mostrar los datos existentes
#     c.execute("SELECT * FROM Radicacion")
#     data = c.fetchall()
#     df = pd.DataFrame(data, columns=['ID', 'Nombre'])
#     st.write("Datos existentes:")
#     st.write(df)
import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('embargos.db')
c = conn.cursor()

st.title("Tipo de Radicacion")

id_radicacion = st.number_input("Ingrese el id de la radicación", min_value=0)
nombre_radicacion = st.text_input("Ingrese el nombre de la radicación")

# Mostrar los datos existentes
c.execute("SELECT * FROM Radicacion")
data = c.fetchall()
df = pd.DataFrame(data, columns=['ID', 'Nombre'])
existing_data_placeholder = st.empty()

if st.button("Guardar"):
    c.execute("INSERT INTO Radicacion (idradicacion, NombreRadicacion) VALUES (?, ?)", (id_radicacion, nombre_radicacion))
    conn.commit()

    # Mostrar los datos existentes actualizados
    c.execute("SELECT * FROM Radicacion")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['ID', 'Nombre'])
    existing_data_placeholder.write("Datos existentes:")
    existing_data_placeholder.write(df)

# Mostrar los datos existentes
existing_data_placeholder.write("Datos existentes:")
existing_data_placeholder.write(df)

# import streamlit as st
# import sqlite3
# from datetime import date
# import pandas as pd

# # Conectarse a la base de datos SQLite
# conn = sqlite3.connect('embargos.db')
# cursor = conn.cursor()

# # Obtener la fecha de hoy
# hoy = date.today()

# # Consulta para obtener los registros de juicios con FechaProximaNotificacion igual a hoy y Finalizado igual a False
# consulta = f"SELECT * FROM Juicios WHERE FechaProximaNotificacion = '{hoy}' AND Finalizado = 'No'"
# cursor.execute(consulta)
# registros = cursor.fetchall()

# # Obtener el total de registros que cumplen con la condición
# total_registros = len(registros)

# # Obtener los nombres de las columnas
# cursor.execute("PRAGMA table_info(Juicios)")
# column_info = cursor.fetchall()
# column_names = [col_info[1] for col_info in column_info]

# # Cerrar la conexión a la base de datos
# conn.close()

# # Mostrar el total de registros en pantalla usando Streamlit
# if registros:
#     # Convertir los registros en un DataFrame
#     df = pd.DataFrame(registros)

#     # Asignar los nombres de las columnas al DataFrame
#     df.columns = column_names

#     # Mostrar el DataFrame en pantalla
#     st.header("Notificaciones del Día de Hoy")
#     st.dataframe(df)

#     # Agregar un formulario para editar el campo "Finalizado" por DNI seleccionado
#     st.subheader("Estado de Notificacion")
#     dni_seleccionado = st.selectbox("Seleccione DNI:", df["Dni"].unique())
#     finalizado = st.selectbox("Finalizado:", ["No", "Si"])

#     # Actualizar la base de datos al presionar el botón "Actualizar"
#     if st.button("Actualizar"):
#         # Conectarse nuevamente a la base de datos
#         conn = sqlite3.connect('embargos.db')
#         cursor = conn.cursor()

#         # Actualizar el campo "Finalizado" en la base de datos
#         cursor.execute(f"UPDATE Juicios SET Finalizado = '{finalizado}' WHERE DNI = '{dni_seleccionado}'")
#         conn.commit()

#         # Cerrar la conexión a la base de datos
#         conn.close()

#         st.success("Registro actualizado correctamente.")

# else:
#     st.write("No se encontraron juicios que cumplan con los criterios de búsqueda.")
import streamlit as st
import sqlite3
from datetime import date, timedelta

import pandas as pd

def notif():
    # Conectarse a la base de datos SQLite
    conn = sqlite3.connect('embargos.db')
    cursor = conn.cursor()

    # Obtener la fecha de hoy
    hoy = date.today()

    # Consulta para obtener los registros de juicios con FechaProximaNotificacion igual a hoy y Finalizado igual a False
    consulta = f"SELECT * FROM Juicios WHERE FechaProximaNotificacion = '{hoy}' AND Finalizado = 'No'"
    cursor.execute(consulta)
    registros = cursor.fetchall()

    # Obtener el total de registros que cumplen con la condición
    total_registros = len(registros)

    # Obtener los nombres de las columnas
    cursor.execute("PRAGMA table_info(Juicios)")
    column_info = cursor.fetchall()
    column_names = [col_info[1] for col_info in column_info]

    # Cerrar la conexión a la base de datos
    conn.close()

    # Mostrar el total de registros en pantalla usando Streamlit
    if registros:
        # Convertir los registros en un DataFrame
        df = pd.DataFrame(registros)

        # Asignar los nombres de las columnas al DataFrame
        df.columns = column_names

        # Mostrar el DataFrame en pantalla
        st.header("Notificaciones del Día de Hoy")
        st.dataframe(df)

        # Agregar un formulario para editar el campo "Finalizado" por DNI seleccionado
        st.subheader("Cambiar Estado de Notificacion")
        dni_seleccionado = st.selectbox("Seleccione DNI:", df["Dni"].unique())
        finalizado = st.selectbox("Finalizado:", ["No", "Si"])

        # Lógica para actualizar las fechas
        if finalizado == "No":
            fecha_notificacion = hoy
            fecha_proxima_notificacion = hoy + timedelta(days=30)
        else:
            fecha_notificacion = hoy
            
            fecha_proxima_notificacion = hoy
        # Actualizar la base de datos al presionar el botón "Actualizar"
        if st.button("Actualizar"):
            # Conectarse nuevamente a la base de datos
            conn = sqlite3.connect('embargos.db')
            cursor = conn.cursor()

            # Actualizar los campos "Finalizado", "FechaUltimaNotificacion" y "FechaProximaNotificacion" en la base de datos
            cursor.execute(f"UPDATE Juicios SET Finalizado = '{finalizado}', FechaUltimaNotificacion = '{fecha_notificacion}', FechaProximaNotificacion = '{fecha_proxima_notificacion}' WHERE DNI = '{dni_seleccionado}'")
            conn.commit()

            # Cerrar la conexión a la base de datos
            conn.close()

            st.success("Registro actualizado correctamente.")

    else:
        st.write("No se encontraron Notificaciones.")

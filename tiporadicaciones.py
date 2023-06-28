
import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('embargos.db')
c = conn.cursor()
st.markdown(
    """
    <style>
        div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
        /* Estilos generales */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f1f1f1;
            margin: 0;
            padding: 0;
        }
        button.step-up {display: none;}
        button.step-down {display: none;}
        div[data-baseweb] {border-radius: 4px;}
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 4px;
        }
        
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        
        /* Estilos del formulario */
        form {
            margin-bottom: 20px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        .form-group input[type="text"],
        .form-group input[type="number"],
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        
        .form-group textarea {
            height: 100px;
            resize: vertical;
        }
        
        .form-submit-button {
            display: block;
            width: 100%;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        
        .form-submit-button:hover {
            background-color: #0056b3;
        }
        
        .success-message {
            margin-top: 20px;
            padding: 10px;
            color: #155724;
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 4px;
        }
        
        .error-message {
            margin-top: 20px;
            padding: 10px;
            color: #721c24;
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            border-radius: 4px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
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

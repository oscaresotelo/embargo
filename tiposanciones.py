import streamlit as st
import pandas as pd
import sqlite3

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

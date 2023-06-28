
import streamlit as st
import sqlite3
from sqlite3 import Error
from streamlit_tags import st_tags
from st_pages import Page, show_pages, add_page_title

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

def create_connection():
    conn = None

    try:
        conn = sqlite3.connect('embargos.db')
        print(f'Successful connection to SQLite version {sqlite3.version}')
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
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
                                            MontoEmbargo REAL
                                        )''')
        print('Successful table creation')
    except Error as e:
        print(e)

def get_radicacion(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT NombreRadicacion FROM Radicacion")
    radicaciones = cursor.fetchall()
    return [r[0] for r in radicaciones]

def get_medidas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT NombreMedida FROM Medidas")
    medidas = cursor.fetchall()
    return [m[0] for m in medidas]

def get_sanciones(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT NombreSancion FROM Sanciones")
    sanciones = cursor.fetchall()
    return [s[0] for s in sanciones]
def get_juzgados(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Localidad FROM Juzgados")
    juzgados = cursor.fetchall()
    return [s[0] for s in juzgados]

def main():

    # título de la página
    st.title('Carga de Embargos')
    show_pages([
        Page("carga.py", "Inicio", ":notebook:"),
        Page("tipomedidas.py", "Tipos de Medidas", ":notebook:"),
        Page("tiporadicaciones.py", "Tipos de Radicaciones", ":notebook:"),
        Page("reportedni.py", "Consulta por Dni", ":notebook:"),
        Page("reportes.py", "Consulta Fecha Inicio", ":notebook:"),
        Page("terminacion.py", "Consulta Beta", ":notebook:"),

    ])
    counter = 1
    c.execute("SELECT id, Localidad FROM Juzgados")
    juzgados_data = c.fetchall()
    juzgado_id = st.selectbox("Selecciona un juzgado", juzgados_data, format_func=lambda x: x[1])
            # juzgado_id = st.selectbox(label='NombreJuzgado', options=juzgados_options)
            
   
    c.execute("SELECT NombreRadicacion FROM Radicacion WHERE Juzgado = ?", (juzgado_id[0],))
    radicaciones_data = c.fetchall()
    rad_judicial = st.selectbox("Selecciona una radicación", radicaciones_data, format_func=lambda x: x[0])

    while True:
        contenedor = st.empty()
        
                
        
    # crear el formulario
        with contenedor.form(key=f'my_form_{counter}'):
            # campos del formulario
            dni = st.number_input(label='Dni', value=0)
            num_expte = st.number_input(label='NumerodeExpte', value=0)
            num_oficio = st.number_input(label='NumeroOficio', value=0)
            medida_options = get_medidas(create_connection())
            medida_cautelar = st.selectbox(label='MedidaCautelar', options=medida_options)
            fecha_inicio = st.date_input(label='FechaInicio')
            observacion = st.text_area(label='Observacion', height=300)
            nombre_juicio = st.text_input(label='NombreJuicio')
            radicacion_options = get_radicacion(create_connection())
            juzgados_options =  get_juzgados(create_connection())
            nominacion_radicacion = st.text_input(label="Nominacion Radicacion")

           
            num_expte_admin = st.number_input(label='NumeroExpteAdministrativo', value=0)
            aclaracion_cautelar = st.text_input(label='AclaracionCautelar')
            fecha_fin = st.date_input(label='FechaFin')
            sanciones_options = get_sanciones(create_connection())
            nombre_sanciones = st.selectbox(label='NombreSanciones', options=sanciones_options)
            monto_embargo = st.number_input(label='MontoEmbargo')
            

            # botón para guardar los datos
            submitted = st.form_submit_button('Guardar Datos')
            if submitted:
                conn = create_connection()
                create_table(conn)

                cursor = conn.cursor()
                
                cursor.execute('''INSERT INTO Juicios 
                                  (Dni, NombreJuicio, NumerodeExpte, RadicacionJudicial, NumeroOficio, 
                                   NumeroExpteAdministrativo, MedidaCautelar, AclaracionCautelar, FechaInicio, 
                                   FechaFin, Observacion, Sanciones, MontoEmbargo, NominacionRadicacion, Juzgado) 
                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                   (dni, nombre_juicio, num_expte, nominacion_radicacion, num_oficio, num_expte_admin,
                                    medida_cautelar, aclaracion_cautelar, fecha_inicio, fecha_fin, observacion,
                                    nombre_sanciones, monto_embargo, rad_judicial[0], juzgado_id[1]))


                conn.commit()
                cursor.close()
                conn.close()

                st.success('Datos guardados exitosamente!')
                contenedor.empty()
                counter += 1  # Incrementar el contador para la siguiente iteración

                continue
        break

if __name__ == '__main__':
    main()

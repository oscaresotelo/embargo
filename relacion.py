import streamlit as st
import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('embargos.db')
c = conn.cursor()

# Crear el formulario
with st.form(key='my_form'):
    # Obtener los datos de la tabla 'juzgados'
    c.execute("SELECT id, Localidad FROM Juzgados")
    juzgados_data = c.fetchall()

    # Crear SelectBox con los datos de la tabla 'juzgados'
    selected_juzgado = st.selectbox("Selecciona un juzgado", juzgados_data, format_func=lambda x: x[1])

    # Guardar el estado de selected_juzgado en st.session_state
    st.session_state.selected_juzgado = selected_juzgado
    st.form_submit_button(label='Enviar')
# Obtener las radicaciones según el juzgado seleccionado
@st.cache_data
def get_radicaciones(juzgado_id):
    # Obtener los datos de la tabla 'radicaciones' relacionados con el juzgado seleccionado
    c.execute("SELECT NombreRadicacion FROM Radicacion WHERE Juzgado = ?", (juzgado_id,))
    radicaciones_data = c.fetchall()
    return radicaciones_data

selected_juzgado = st.session_state.selected_juzgado
radicaciones_data = get_radicaciones(selected_juzgado[0]) if selected_juzgado else []

# Crear SelectBox con los datos de la tabla 'radicaciones'
selected_radicacion = st.selectbox("Selecciona una radicación", radicaciones_data, format_func=lambda x: x[0])

# Cerrar la conexión a la base de datos
conn.close()

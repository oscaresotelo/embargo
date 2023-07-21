import streamlit as st
import sqlite3
from st_aggrid import AgGrid , GridUpdateMode

from st_aggrid.grid_options_builder import GridOptionsBuilder 

import pandas as pd

# Conexión a la base de datos
conn = sqlite3.connect('embargos.db')
c = conn.cursor()

# Función para buscar registros en la tabla Juicios por DNI
@st.cache_data
def buscar_juicios_por_dni(dni):
    c.execute("SELECT * FROM Juicios WHERE Dni=?", (dni,))
    juicios = c.fetchall()
    return(juicios)
    # df = pd.DataFrame(juicios, columns=["id", "Dni", "NombreJuicio", "NumerodeExpte", "RadicacionJudicial", "NumeroOficio", "NumeroExpteAdministrativo", "MedidaCautelar", "AclaracionCautelar", "FechaInicio", "FechaFin", "Observacion", "MontoEmbargo", "Sanciones", "NominacionRadicacion", "Juzgado"])
    # gd = GridOptionsBuilder.from_dataframe(df)
    # gd.configure_pagination(enabled=True)
    # gd.configure_default_column(editable=True, groupable=True)
    # sel_mode = st.radio("Seleccione ", options = ["uno", "multiples"])
    # gd.configure_selection(selection_mode = sel_mode ,use_checkbox=True)
    # gridoptions = gd.build() 
    # AgGrid(df, gridOptions=gridoptions)

# Título de la aplicación
st.title('Búsqueda de Juicios por DNI')

# Formulario para ingresar el DNI
dni = st.text_input('Ingrese el DNI')

# Botón para realizar la búsqueda
if st.button('Buscar'):
    if dni:
        # Realizar la búsqueda en la base de datos
        if "juicios" not in st.session_state:
            st.session_state.juicios = ""
        juicios = buscar_juicios_por_dni(dni)
        df = pd.DataFrame(juicios, columns=["id", "Dni", "NombreJuicio", "NumerodeExpte", "RadicacionJudicial", "NumeroOficio", "NumeroExpteAdministrativo", "MedidaCautelar", "AclaracionCautelar", "FechaInicio", "FechaFin", "Observacion", "MontoEmbargo", "Sanciones", "NominacionRadicacion", "Juzgado", "FechaUltimaNotificacion","FechaProximaNotificacion","Finalizado"])
        st.session_state.juicios = df
        
gd = GridOptionsBuilder.from_dataframe(st.session_state.juicios)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True, groupable=True)
sel_mode = st.radio("Seleccione ", options = ["uno", "multiples"])
gd.configure_selection(selection_mode = sel_mode ,use_checkbox=True)
gridoptions = gd.build() 
grid_table = AgGrid(st.session_state.juicios, gridOptions=gridoptions,
                    update_mode = GridUpdateMode.SELECTION_CHANGED,
                    height = 500,
                    allow_unsafe_jscode = True,
                    
                    )
sel_row = grid_table["selected_rows"]
st.write(sel_row)

        # Mostrar los resultados en pantalla
    #     if juicios:
    #         st.write('Juicios encontrados:')
           
    #     else:
    #         st.write('No se encontraron juicios para el DNI ingresado.')
    # else:
    #     st.write('Por favor, ingrese un DNI válido.')

# Cerrar la conexión a la base de datos
conn.close()

import streamlit as st

def buscar_articulo(articulo_numero):
    with open('codigocivilycomercial.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for i, linea in enumerate(lineas):
            if linea.startswith(f'ARTICULO {articulo_numero}'):
                resultado = linea
                j = i + 1
                while j < len(lineas) and not lineas[j].startswith('ARTICULO'):
                    resultado += lineas[j]
                    j += 1
                return resultado
        return None

st.title('Búsqueda de Artículo')

numero_articulo = st.number_input('Ingrese el número de artículo:', min_value=1, value=1, step=1)
articulo_encontrado = buscar_articulo(numero_articulo)

if articulo_encontrado:
    st.write(articulo_encontrado)
else:
    st.write('El artículo especificado no fue encontrado en el archivo.')

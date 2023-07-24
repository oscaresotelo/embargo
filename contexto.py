"""
This file contains the template for the prompt to be used for injecting the context into the model.

With this technique we can use different plugin for different type of question and answer.
Like :
- Internet
- Data
- Code
- PDF
- Audio
- Video

"""

from datetime import datetime
now = datetime.now()

def explicacion(prompt,context):
    final_prompt = f""" 
                        INSTRUCCIÓN: EN TU RESPUESTA, DEBES INCLUIR LA RESPUESTA EL ARTICULO ORIGINAL , EXPLICAR CADA ARTICULO QUE FIGURA 
                        UNO POR UNO, 
                        ESCRIBE SIEMPRE SOLO TU RESPUESTA PRECISA EN LA SIGUIENTE LINEA
                        CONTEXTO : ({context})
                        AHORA EL USUARIO PREGUNTA : {prompt} . 
                        ESCRIBE LA RESPUESTA :"""
    return final_prompt
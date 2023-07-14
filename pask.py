import sketch
import pandas as pd

df = pd.read_csv("maestro.csv")
respuesta = df.sketch.ask("de que trata el archivo? ",call_display=False)
print(respuesta)
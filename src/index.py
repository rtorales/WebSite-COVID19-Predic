from flask import Flask, render_template
import numpy as np
import pandas as pd
import datos

app = Flask(__name__)

#Obtener Datos Estadísticos
datos = datos.ObtenerValores()
#array de Datos Estadísticos
datosChart = datos.to_numpy()
#i = 0
#for row in datosChart:
#    print(datosChart[i][1])
#    i += 1
#     
#\s+
#página principal
@app.route('/')
def home():
    print(datosChart)
    return render_template('home.html', tables=[datos.to_html(classes='data')], titles=datos.columns.values, values=datosChart)

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

if __name__ == "__main__":
    app.run(debug=True)

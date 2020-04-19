import csv
import pandas as pd
from datetime import datetime,date,timedelta
import calculos

def ObtenerValores():
    #fuente datos COVID19
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    datos = pd.DataFrame(pd.read_csv(url, header=0))
    #solo Abril en Adelante
    datos = datos[datos['date'] >= '2020-04-01'][['iso_code','date', 'total_cases']]
    #Obtener Datos Calculados
    DatosParaguay = calculos.__CalcularValoresParaguay__(datos)
    DatosArgentina = calculos.__CalcularValoresArgentina__(datos)
    DatosBrasil = calculos.__CalcularValoresBrasil__(datos)
    DatosUruguay = calculos.__CalcularValoresUruguay__(datos)

    #tabla Comparativa
    TablaComparativa = pd.concat(
        [DatosParaguay, DatosArgentina['Argentina'], DatosBrasil['Brasil'], DatosUruguay['Uruguay']], axis=1)
    TablaComparativa.rename(columns={'date': 'Fecha'}, inplace=True)

    #cambiar a Tasa de Infectados (al ser contantes, se copio y pegó, pueden obtenerse de manera automática)
    #fuente: http://datatopics.worldbank.org/world-development-indicators/
    PoblacionPy = 6956000
    PoblacionAr = 44490000
    PoblacionBr = 209500000
    PoblacionUy = 3449000
    TablaComparativa.loc[:, 'Paraguay'] /= PoblacionPy
    TablaComparativa.loc[:, 'Argentina'] /= PoblacionAr
    TablaComparativa.loc[:, 'Brasil'] /= PoblacionBr
    TablaComparativa.loc[:, 'Uruguay'] /= PoblacionUy

    #devolver Valor
    return TablaComparativa

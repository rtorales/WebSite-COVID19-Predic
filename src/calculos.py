import csv
import pandas as pd
from datetime import datetime, date, timedelta

#Cálculo de Paraguay
def __CalcularValoresParaguay__(datos):
    DatosParaguay = datos[datos['iso_code'] == 'PRY'][['date', 'total_cases']]
    ValorAnterior = 0
    ValorActual = 0
    contador = 0
    SumaFactor = 0
    for columna, contenido in DatosParaguay.items():
        if (columna == 'total_cases'):
            for row in contenido:
                if (ValorAnterior == 0):
                    ValorAnterior = row
                    if (ValorAnterior == 0):
                        #print('No hay contagiados')
                        continue
                if (row == 0):
                    ValorActual = ValorAnterior
                else:
                    ValorActual = row
                    contador += 1
                SumaFactor += ValorActual/ValorAnterior
                #print('el Factor es: {}'.format(ValorActual/ValorAnterior))
                ValorAnterior = ValorActual
    #print('La suma de los factores es: {}'.format(SumaFactor))
    #print('De un total de: {}'.format(contador))
    FactorPromedio = SumaFactor/contador
    #print('Factor Promedio: {}'.format(FactorPromedio))
    #incluir proyección de 10 días
    #Obtener último Caso y valores
    total_cases = pd.unique(DatosParaguay.tail(1)['total_cases'])[0]
    ultimo_dia = pd.unique(DatosParaguay.tail(1)['date'])[0]
    ultimo_dia = datetime.strptime(ultimo_dia, '%Y-%m-%d')
    for i in range(0, 11):
        #sumar un día
        ultimo_dia = ultimo_dia + timedelta(days=1)
        #nuevos Casos
        total_cases = total_cases * FactorPromedio
        #append al frame de valores
        DatosParaguay = DatosParaguay.append({'date': ultimo_dia.strftime(
            '%Y-%m-%d'), 'total_cases': total_cases}, ignore_index=True)
    #mostrar Datos
    DatosParaguay.rename(columns={'total_cases': 'Paraguay'}, inplace=True)
    #cambiar casos a tasa de infectados
    #DatosParaguay['total_cases'] = DatosParaguay['total_cases'].apply(lambda x: x/Poblacion)
    return DatosParaguay

#Cálculo de Argentina
def __CalcularValoresArgentina__(datos):
    DatosArgentina = datos[datos['iso_code'] == 'ARG'][['date', 'total_cases']]
    ValorAnterior = 0
    ValorActual = 0
    contador = 0
    SumaFactor = 0
    for columna, contenido in DatosArgentina.items():
        if (columna == 'total_cases'):
            for row in contenido:
                if (ValorAnterior == 0):
                    ValorAnterior = row
                    if (ValorAnterior == 0):
                        #print('No hay contagiados')
                        continue
                if (row == 0):
                    ValorActual = ValorAnterior
                else:
                    ValorActual = row
                    contador += 1
                SumaFactor += ValorActual/ValorAnterior
                #print('el Factor es: {}'.format(ValorActual/ValorAnterior))
                ValorAnterior = ValorActual
    #print('La suma de los factores es: {}'.format(SumaFactor))
    #print('De un total de: {}'.format(contador))
    FactorPromedio = SumaFactor/contador
    #print('Factor Promedio: {}'.format(FactorPromedio))
    #incluir proyección de 10 días
    #Obtener último Caso y valores
    total_cases = pd.unique(DatosArgentina.tail(1)['total_cases'])[0]
    ultimo_dia = pd.unique(DatosArgentina.tail(1)['date'])[0]
    ultimo_dia = datetime.strptime(ultimo_dia, '%Y-%m-%d')
    for i in range(0, 11):
        #sumar un día
        ultimo_dia = ultimo_dia + timedelta(days=1)
        #nuevos Casos
        total_cases = total_cases * FactorPromedio
        #append al frame de valores
        DatosArgentina = DatosArgentina.append({'date': ultimo_dia.strftime(
            '%Y-%m-%d'), 'total_cases': total_cases}, ignore_index=True)
    #mostrar Datos
    DatosArgentina.rename(columns={'total_cases': 'Argentina'}, inplace=True)
    return DatosArgentina

#Cálculo de Brasil
def __CalcularValoresBrasil__(datos):
    DatosBrasil = datos[datos['iso_code'] == 'BRA'][['date', 'total_cases']]
    ValorAnterior = 0
    ValorActual = 0
    contador = 0
    SumaFactor = 0
    for columna, contenido in DatosBrasil.items():
        if (columna == 'total_cases'):
            for row in contenido:
                if (ValorAnterior == 0):
                    ValorAnterior = row
                    if (ValorAnterior == 0):
                        #print('No hay contagiados')
                        continue
                if (row == 0):
                    ValorActual = ValorAnterior
                else:
                    ValorActual = row
                    contador += 1
                SumaFactor += ValorActual/ValorAnterior
                #print('el Factor es: {}'.format(ValorActual/ValorAnterior))
                ValorAnterior = ValorActual
    #print('La suma de los factores es: {}'.format(SumaFactor))
    #print('De un total de: {}'.format(contador))
    FactorPromedio = SumaFactor/contador
    #print('Factor Promedio: {}'.format(FactorPromedio))
    #incluir proyección de 10 días
    #Obtener último Caso y valores
    total_cases = pd.unique(DatosBrasil.tail(1)['total_cases'])[0]
    ultimo_dia = pd.unique(DatosBrasil.tail(1)['date'])[0]
    ultimo_dia = datetime.strptime(ultimo_dia, '%Y-%m-%d')
    for i in range(0, 11):
        #sumar un día
        ultimo_dia = ultimo_dia + timedelta(days=1)
        #nuevos Casos
        total_cases = total_cases * FactorPromedio
        #append al frame de valores
        DatosBrasil = DatosBrasil.append({'date': ultimo_dia.strftime(
            '%Y-%m-%d'), 'total_cases': total_cases}, ignore_index=True)
    #mostrar Datos
    DatosBrasil.rename(columns={'total_cases': 'Brasil'}, inplace=True)
    return DatosBrasil

#Cálculo de Uruguay
def __CalcularValoresUruguay__(datos):
    DatosUruguay = datos[datos['iso_code'] == 'URY'][['date', 'total_cases']]
    ValorAnterior = 0
    ValorActual = 0
    contador = 0
    SumaFactor = 0
    for columna, contenido in DatosUruguay.items():
        if (columna == 'total_cases'):
            for row in contenido:
                if (ValorAnterior == 0):
                    ValorAnterior = row
                    if (ValorAnterior == 0):
                        #print('No hay contagiados')
                        continue
                if (row == 0):
                    ValorActual = ValorAnterior
                else:
                    ValorActual = row
                    contador += 1
                SumaFactor += ValorActual/ValorAnterior
                #print('el Factor es: {}'.format(ValorActual/ValorAnterior))
                ValorAnterior = ValorActual
    #print('La suma de los factores es: {}'.format(SumaFactor))
    #print('De un total de: {}'.format(contador))
    FactorPromedio = SumaFactor/contador
    #print('Factor Promedio: {}'.format(FactorPromedio))
    #incluir proyección de 10 días
    #Obtener último Caso y valores
    total_cases = pd.unique(DatosUruguay.tail(1)['total_cases'])[0]
    ultimo_dia = pd.unique(DatosUruguay.tail(1)['date'])[0]
    ultimo_dia = datetime.strptime(ultimo_dia, '%Y-%m-%d')
    for i in range(0, 11):
        #sumar un día
        ultimo_dia = ultimo_dia + timedelta(days=1)
        #nuevos Casos
        total_cases = total_cases * FactorPromedio
        #append al frame de valores
        DatosUruguay = DatosUruguay.append({'date': ultimo_dia.strftime(
            '%Y-%m-%d'), 'total_cases': total_cases}, ignore_index=True)
    #mostrar Datos
    DatosUruguay.rename(columns={'total_cases': 'Uruguay'}, inplace=True)
    return DatosUruguay

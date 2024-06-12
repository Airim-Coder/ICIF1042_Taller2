'''
Autor: Maria Paz Cisternas Pardo
Version: 24.06.09
Contenido:
1. Cargar los datos de ventas y clientes desde los archivos CSV generados utilizando Pandas y almacenarlos en DataFrames separados.
2. Realizar una limpieza de datos inicial en ambos DataFrames, manejando los valores nulos y convirtiendo los tipos de datos según sea necesario.
   Documentar en el informe los pasos realizados para la limpieza de datos. Realizar una limpieza de datos inicial en ambos DataFrames, 
   manejando los valores nulos y convirtiendo los tipos de datos según sea necesario. Documentar en el informe los pasos realizados para la limpieza de datos. 
'''
import csv, os
import pandas as pd
import numpy as np

def Limpiar_Datos():
    df_ventas = LeerArchivo("ventas.csv")
    df_clientes = LeerArchivo("clientes.csv")
    print(df_ventas)
    print(df_clientes)
    
    Analisis_NaN(df_ventas, 'ventas')
    Analisis_NaN(df_clientes, 'clientes')

def LeerArchivo(archivo):  #funcion para leer el archivo csv
    try:
        df_datos = pd.read_csv(archivo)
        return df_datos
    except FileNotFoundError: #control de error si el archivo no existe
        raise(f"Error: Archivo '{archivo}' no encontrado.")

def Analisis_NaN(data, nombre):
    #Análisis de valores nulos
    print(f"Análisis de valores nulos en {nombre}:")
    print(data.info())
    porcentaje_NaN = data.isna().sum() / len(data) * 100
    print(porcentaje_NaN)
    
    #Análisis de patrones de falta
    data.isna().sum(axis=0)
    
    #Eliminación de filas con alto porcentaje de NaN
    data.dropna(thresh=0.5, inplace=True)
    
    #Imputación de valores faltantes con la media
    if nombre == 'ventas':
        #data["Producto"].fillna(data["Producto"].mean(), inplace=True)
        data["Producto"].hist() #Distribución despues de la imputacion
    elif nombre.lower == 'clientes':
        #data["Nombre"].fillna(data["Nombre"].mean(), inplace=True)
        data["Edad"].fillna(data["Edad"].mean(), inplace=True)
        #Distribución despues de la imputacion
        data["Nombre"].hist()
        data["Edad"].hist()

    #Guardado del df limpio
    cleaner_df = data
    return cleaner_df

def main(): #Solo para depuracion
    Limpiar_Datos()

if __name__ == "__main__":
    main()
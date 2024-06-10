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
    

def LeerArchivo(archivo):  #funcion para leer el archivo csv
    try:
        df_datos = pd.read_csv(archivo)
        return df_datos
    except FileNotFoundError: #control de error si el archivo no existe
        raise(f"Error: Archivo '{archivo}' no encontrado.")

def Limpiar_Ventas(ventas): ##pruebas
    #Manejo de valores nulos
    ventas.dropna(inplace=True) #eliminar filas con valores nulos
    #Conversion de tipos de datos
    ventas['Fecha'] = pd.to_datetime(ventas['Fecha']) #convertir columna Fecha a
    ventas['Valor'] = pd.to_numeric(ventas['Valor'], errors='coerce') #
    return ventas

def main(): #Solo para depuracion
    Limpiar_Datos()

if __name__ == "__main__":
    main()
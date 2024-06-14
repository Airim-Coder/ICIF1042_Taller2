'''
Autor: Maria Paz Cisternas Pardo
Version: 24.06.09
Contenido:
1. Cargar los datos de ventas y clientes desde los archivos CSV generados utilizando Pandas y almacenarlos en DataFrames separados.
2. Realizar una limpieza de datos inicial en ambos DataFrames, manejando los valores nulos y convirtiendo los tipos de datos según sea necesario.
   Documentar en el informe los pasos realizados para la limpieza de datos.
'''
import csv, os
import pandas as pd
import numpy as np
#import matplotlib 

def LeerArchivo(archivo):  #funcion para leer el archivo csv
    try:
        df_datos = pd.read_csv(archivo)
        return df_datos
    except FileNotFoundError: #control de error si el archivo no existe
        raise(f"Error: Archivo '{archivo}' no encontrado.")

def Limpiar_Datos(data, nombre):
    filas= data.shape[0]
    total_nan = data.isnull().sum().sum()
    p_nan = (total_nan/filas)*100
    
    if p_nan <= 5 and nombre == 'clientes':
        data.dropna(thresh=1, inplace=True)
        print(f"Las filas de '{nombre}' que contengan valores NULL serán eliminadas ")
    elif p_nan > 5 and nombre == 'ventas':
        data["Producto"].fillna(data["Producto"].mode()[0], inplace=True)
        print(f"Las filas de '{nombre}' que contengan valores NULL serán imputadas con la Moda ")
    else:
        print(f"No se realizará limpieza de datos en '{nombre}' al no coincidir con los parametros trabajados")
    cleaned_data = data
    return cleaned_data

def Conversion_Datos(data, nombre): #Conversion de los datos contenidos para un mejor analisis posterior
    if nombre == 'ventas':
        data['ID_Venta']=round(data['ID_Venta'].astype(int))
        data['ID_Cliente']=round(data['ID_Cliente'].astype(int))
        data['Categoría']=data['Categoría'].to_string()
        data['Producto']=data['Producto'].to_string()
        data['Precio']=round(data['Precio'].astype(int))
        data['Cantidad']=round(data['Cantidad'].astype(int))
    elif nombre == 'clientes':
        data['ID_Cliente']=round(data['ID_Cliente'].astype(int))
        data['Nombre']=data['Nombre'].to_string()
        data['Edad']=round(data['Edad'].astype(int))
        data['Genero']=round(data['Genero'].to_string())
        data['Ubicacion']=round(data['Ubicacion'].to_string())
    return data
    

def main(): #Solo para depuracion
    print("do something")
if __name__ == "__main__":
    main()
'''
Autor: Maria Paz Cisternas Pardo
Version: 24.06.09
Contenido:
1. Cargar los datos de ventas y clientes desde los archivos CSV generados utilizando Pandas y almacenarlos en DataFrames separados.
2. Realizar una limpieza de datos inicial en ambos DataFrames, manejando los valores nulos y convirtiendo los tipos de datos según sea necesario.
   Documentar en el informe los pasos realizados para la limpieza de datos.
'''
import pandas as pd
import numpy as np


def LeerArchivo(archivo):  #funcion para leer el archivo csv
    try:
        df_datos = pd.read_csv(archivo)
        return df_datos
    except FileNotFoundError: #control de error si el archivo no existe
        raise(f"Error: Archivo '{archivo}' no encontrado.")

def Limpiar_Datos(data, nombre): #funcion que limpia datos ya sea por eliminacion o imputacion de acuerdo al caso
    while(data.isnull().any().any()): # mientras existan datos nulos ejecutara la imputacion o eliminacion
        filas= data.shape[0]
        total_nan = data.isnull().sum().sum()
        p_nan = (total_nan/filas)*100 # porcentaje de nulos
        
        if p_nan <= 5: # si el porcentaje de nulos es menor o igual a 5%
            data.dropna(inplace=True)# eliminacion de nulos
            print(f"Las filas de '{nombre}' que contengan valores NULL serán eliminadas ")
        elif p_nan > 5: # si el porcentaje de nulos es mayor a 5%
            if nombre == 'ventas': 
                data["Producto"].fillna(data["Producto"].mode()[0], inplace=True)
                print(f"Las filas de '{nombre}' columna 'Producto' que contengan valores NULL serán imputadas con la Moda ")
            elif nombre == 'clientes':
                data["Edad"].fillna(data["Edad"].mean(), inplace=True)
                print(f"Las filas de '{nombre}' columna 'Edad' que contengan valores NULL serám imputadas con la Media")
                data["Nombre"].fillna(data["Nombre"].mode()[0], inplace=True)
                print(f"Las filas de '{nombre}' columna 'Nombre' que contengan valores NULL serám imputadas con la Moda")
        else:
            print(f"No se realizará limpieza de datos en '{nombre}' al no coincidir con los parametros trabajados")
    cleaned_data = data
    return cleaned_data

def Conversion_Datos(data, nombre): #Conversion de los datos contenidos para un mejor analisis posterior
    if nombre == 'ventas':
        data['ID_Venta']=data['ID_Venta'].astype(int).round()
        data['ID_Cliente']=data['ID_Cliente'].astype(int).round()
        data['Categoría']=data['Categoría'].astype(str)
        data['Producto']=data['Producto'].astype(str)
        data['Precio']=data['Precio'].astype(int).round()
        data['Cantidad']=data['Cantidad'].astype(int).round()
    elif nombre == 'clientes':
        data['ID_Cliente']=data['ID_Cliente'].astype(int).round()
        data['Nombre']=data['Nombre'].astype(str)
        data['Edad']=data['Edad'].astype(int).round()
        data['Genero']=data['Genero'].astype(str)
        data['Ubicacion']=data['Ubicacion'].astype(str)
    return data

def main(): #Solo para depuracion
    print("do something")
if __name__ == "__main__":
    main()
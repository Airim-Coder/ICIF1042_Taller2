#Generacion de Archivos CSV para ventas
'''
Autor: Maria Paz Cisternas Pardo
Version: 24.06.01
Contenido:
1. Generar dos archivos CSV llamados "ventas.csv" y "clientes.csv" que contengan los datos de ventas y clientes, respectivamente. 
2. Los datos deben ser generados aleatoriamente utilizando funciones de probabilidad (indique en su informe que distribución uso: uniforme, normal u otra).
3. Los valores nulos deben representarse con la palabra "NULL". En el archivo "ventas.csv"
    - La columna "Producto" puede contener hasta un 10% de valores nulos. 
    - En el archivo "clientes.csv", las columnas "Nombre" y "Edad" pueden contener hasta un 5% de valores nulos cada una.
'''
import faker as fk 
import pandas as pd
import numpy as np
import os, random, csv

def DataGen_Cliente(num_clientes):
    #region Generacion de datos de clientes
    nombres = NameListGen(num_clientes) #Generación de nombre para 125 clientes
    edad = range(18,80) #Generacion de Edad entre los 18 y 80 años
    genero = ['Femenino','Masculino']
    ubicacion = ['Norte','Sur','Este','Oeste']
    #endregion
    try:
        clientes = pd.DataFrame({
            "ID_Cliente": np.arange(1, num_clientes +1),
            "Nombre": [random.choices(nombres) if random.random() > 0.05 else "NULL" for i in range(num_clientes)],
            "Edad": [random.choices(edad) if random.random() > 0.05 else "NULL" for i in range(num_clientes)],
            "Genero": [random.choice(genero)],
            "Ubicacion": [random.choice(ubicacion)]
        })
        return clientes
    except:
        print("Ha surgido un error en la generacion de clientes")

def DataGen_Ventas(num_ventas):
    #region Generacion de datos de ventas
    #ID_Venta,ID_Cliente,Producto,Categoría,Precio,Cantidad
    try:
         ventas = pd.DataFrame({})
         return ventas
    except:
        print("Ha surgido un error en la generacion de ventas")
    #endregion
        

#region INTERNAL
def NameListGen(clientes):
    nombres_comunes=[]
    for i in range(clientes):
        name = fk.Faker().name()
        nombres_comunes.append(name)
    return nombres_comunes

def ProductsListGen():
    print()
#endregion


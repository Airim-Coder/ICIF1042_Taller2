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
#from faker import Faker
import pandas as pd
import numpy as np
import os, random

def Simulador_Ventas(num_ventas,num_clientes):
    clientes = DataGen_Clientes(num_clientes)
    FileWrite('clientes.csv', clientes)
                 
    ventas = DataGen_Ventas(num_ventas, clientes)
    FileWrite('ventas.csv',ventas)

def DataGen_Clientes(num_clientes): #Genera clientes aleatorios segun los parametros ingresados
    try:
        df_clientes = pd.DataFrame(columns=['ID_Cliente','Nombre','Edad','Genero','Ubicacion'])
        clientes_genero = _clientListGen()
        for _ in range(num_clientes):
            nombres = _clientGen(clientes_genero)#_nameListGen(num_clientes)
            df_clientes = df_clientes._append(nombres, ignore_index=True)
            
        df_clientes['ID_Cliente']= np.arange(1, len(df_clientes)+1)
        return df_clientes
    except:
        raise Exception("Ha surgido un error en la generacion de clientes")

def DataGen_Ventas(num_ventas, clientes): #Genera ventas aleatorias segun los parametros ingresados
    #region Generacion de datos de ventas
    categorias_productos = _productList()
    lista_clientes = list(clientes['ID_Cliente'])
    #endregion
    try:
        df_ventas= pd.DataFrame(columns=["ID_Venta","ID_Cliente","Categoría", "Producto", "Precio", "Cantidad"])
        for _ in range(num_ventas):
            venta = _saleGen(categorias_productos, num_ventas)
            df_ventas['ID_Cliente'] = df_ventas.apply(lambda row: random.choice(lista_clientes), axis=1)
            df_ventas = df_ventas._append(venta, ignore_index=True)
            
        df_ventas['ID_Venta'] = range(1, len(df_ventas) + 1)
        return df_ventas
    except:
        raise Exception("Ha surgido un error en la generacion de ventas")

def FileWrite(nombre,datos): #Escribe los datos en un archivo CSV
    try:
        # Verifica si existe archivo CSV y lo elimina
        if os.path.exists('data/'+nombre):# Elimina archivo CSV si existe en el directorio
            os.remove('data/'+nombre)

        # Genera un nuevo archivo CSV con datos
        datos.to_csv('data/'+nombre, index=False)
        print(f"Archivo '{nombre}' generado con exito")
    except:
        raise("Ha surgido un error escribiendo el archivo")

#region INTERNAL
def _clientListGen():
    nombres = {
        "Mitchell": {'Genero': 'Masculino'},
        "Lily": {"Genero": "Femenino"},
        "Ethan": {"Genero": "Masculino"},
        "Ava": {"Genero": "Femenino"},
        "Jesus":{"Genero": "Masculino"},
        "Olivia": {"Genero": "Femenino"},
        "Noah": {"Genero": "Masculino"},
        "Evelyn": {"Genero": "Femenino"},
        "Liam": {"Genero": "Masculino"},
        "Sophia": {"Genero": "Femenino"},
        "Daniel":{"Genero": "Masculino"},
        "Maria":{"Genero": "Femenino"},
        }
    return nombres

def _clientGen(nombres):
    nombre = random.choice(list(nombres.keys()))
    apellidos =["Robertson","Tran","Patel","Lee","Floyd","Brown","White","Hall","Martin","Davis","Lambert","Scott"]
    genero_sin_asig = ["Femenino","Masculino","Otro"]
    
    #Distribucion Bernoulli
    if random.random() < 0.05:
        nombre = 'NULL'
        genero = random.choice(genero_sin_asig)
    else:
        nombre = nombre
        genero = nombres[nombre]["Genero"]
        nombre = nombre + ' ' +random.choice(apellidos)
    
    if random.random() < 0.05:
       edad = 'NULL'
    else:
        edad = random.randint(18, 65) #Distribucion Uniforme
    ubicacion = random.choice(["Norte","Sur","Centro","Este","Oeste"])
    
    return {"Nombre":nombre, "Genero": genero, 'Edad': edad, 'Ubicacion': ubicacion}

'''def _nameListGen(clientes): #Uso de lib Faker
    fake = Faker()
    nombres_comunes=[]
    for i in range(clientes):
        name = fake.name()
        nombres_comunes.append(name)
    return nombres_comunes'''

def _productList():
    categorias_productos = {
            "Hogar": {
                "Productos": {"Refrigerador", "Estufa Eléctrica", "Lavadora", "Horno Eléctrico"}
            },
            "Electrónica": {
                "Productos": {"Televisor", "Laptop", "Computadora", "Tablet", "Teléfono"}
            },
            "Electrodomesticos": {
                "Productos": {"Licuadora", "Batidora", "Cafetera", "Tostadora"}
            },
            "Tecnologia": {
                "Productos": {"Audífonos", "Cámara", "Lámpara", "Bateria"}
            }
        }
    return categorias_productos

def _saleGen(categorias_productos,num_ventas):
    
    
    categoria = random.choice(list(categorias_productos.keys()))
    productos = list(categorias_productos[categoria]["Productos"])
    
    
    #Distribución Normal
    if categoria in ("Electrodomesticos","Tecnologia"):
       x = 9611 # Media para productos relativamente baratos
       s = 10652 # Desviacion Estandar para productos relativamente baratos
    else:
        x = 227493  # Media para productos relativamente caros
        s = 180016 # Desviacion Estandar para productos relativamente caros
    dn = np.random.normal(loc=x,scale=s,size=num_ventas)
    precios = dn[dn>0] # eliminacion de valores negativos de la campana
    
    #Distribucion Bernoulli
    if random.random() < 0.1:
        producto = 'NULL'
    else:
        producto = random.choice(productos)

    precio = np.random.choice(precios)
    cantidad = random.randint(1, 5)

    return {"Categoría": categoria, "Producto": producto, "Precio": precio, "Cantidad": cantidad}
#endregion

def main(): #Solo para depuracion
    Simulador_Ventas(10,5)

if __name__ == "__main__":
    main()

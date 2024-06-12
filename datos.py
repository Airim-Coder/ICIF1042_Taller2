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

def DataGen_Clientes(num_clientes):
    try:
        df_clientes = pd.DataFrame(columns=['ID_Cliente','Nombre','Edad','Genero','Ubicacion'])
        clientes_genero = _clientListGen()
        for _ in range(num_clientes):
            nombres = _clientGen(clientes_genero)#_nameListGen(num_clientes)
            df_clientes['ID_Cliente']= range(1, len(df_clientes) + 1)
            df_clientes = df_clientes._append(nombres, ignore_index=True)
        return df_clientes
    except:
        raise Exception("Ha surgido un error en la generacion de clientes")

def DataGen_Ventas(num_ventas, clientes):
    #region Generacion de datos de ventas
    categorias_productos = _productList()
    lista_clientes = list(clientes['ID_Cliente'])
    #endregion
    try:
        df_ventas= pd.DataFrame(columns=["ID_Venta","ID_Cliente","Categoría", "Producto", "Precio", "Cantidad"])
        for _ in range(num_ventas):
            venta = _saleGen(categorias_productos)
            df_ventas['ID_Venta'] = range(1, len(df_ventas) + 1)
            df_ventas['ID_Cliente'] = df_ventas.apply(lambda row: random.choice(lista_clientes), axis=1)
            df_ventas = df_ventas._append(venta, ignore_index=True)
        return df_ventas
    except:
        raise Exception("Ha surgido un error en la generacion de ventas")

def FileWrite(nombre,datos): #Escribe los datos en un archivo CSV
    try:
        # Verifica si existe archivo CSV y lo elimina
        if os.path.exists(nombre):# Elimina archivo CSV si existe en el directorio
            os.remove(nombre)

        # Genera un nuevo archivo CSV con datos
        datos.to_csv(nombre, index=False)
        print("Archivo CSV generado con exito")
    except:
        raise("Ha surgido un error escribiendo el archivo")

#region INTERNAL
def _clientListGen():
    clientes_genero = {
        "Mitchell Robertson": {'Genero': 'Masculino'},
        "Lily Tran": {"Genero": "Femenino"},
        "Ethan Patel": {"Genero": "Masculino"},
        "Ava Lee": {"Genero": "Femenino"},
        "Jesus Floyd":{"Genero": "Masculino"},
        "Olivia Brown": {"Genero": "Femenino"},
        "Noah White": {"Genero": "Masculino"},
        "Evelyn Hall": {"Genero": "Femenino"},
        "Liam Martin": {"Genero": "Masculino"},
        "Sophia Davis": {"Genero": "Femenino"},
        "Daniel Lambert":{"Genero": "Masculino"},
        "Maria Scott":{"Genero": "Femenino"},
        }
    return clientes_genero

def _clientGen(clientes_genero):
    nombre = random.choice(list(clientes_genero.keys()))
    genero_sin_asig = ["Femenino","Masculino","Otro"]
    if random.random() < 0.05:
        nombre = None
        genero = random.choice(genero_sin_asig)
    else:
        nombre = random.choice(nombre)
        genero = list(clientes_genero[nombre]["Genero"])
    
    if random.random() < 0.05:
       edad = None 
    else:
        edad = random.randint(18, 65)
    ubicacion = random.choice(["Norte","Sur","Este","Oeste"])
    
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
            "Productos": {"Refrigerador":{"Precio": 199990},"Estufa Electrica":{"Precio": 129990}, "Lavadora":{"Precio": 164990}, "Horno Electrico":{"Precio": 189990}, "Lámpara":{"Precio": 4990}}},
            "Electrónica": {
            "Productos": {"Televisor":{"Precio": 159990},
            "Laptop":{"Precio": 699990}, "Computadora":{"Precio": 360608}, "Tablet":{"Precio": 179990}, "Telefono":{"Precio": 296404}, "Licuadora":{"Precio": 19990}, "Batidora":{"Precio": 29990}, "Cafetera":{"Precio": 59990}, "Tostadora":{"Precio": 24990}, "Audífonos":{"Precio": 12990}, "Cámara":{"Precio": 60490}}  
          }
        }
    return categorias_productos
def _saleGen(categorias_productos):
    categoria = random.choice(list(categorias_productos.keys()))
    productos = list(categorias_productos[categoria]["Productos"].keys())
    precios_sin_cat= [1000,1300,1500,1990, 2990,3990,4990]
    if random.random() < 0.1:
        producto = None
        precio = random.choice(precios_sin_cat)
    else:
        producto = random.choice(productos)
        precio = categorias_productos[categoria]["Productos"][producto]["Precio"]
        
    cantidad = random.randint(1, 5)

    return {"Categoria": categoria, "Producto": producto, "Precio": precio, "Cantidad": cantidad}
#endregion

def main(): #Solo para depuracion
    Simulador_Ventas(10,5)

if __name__ == "__main__":
    main()

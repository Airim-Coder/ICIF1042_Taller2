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
from faker import Faker
import pandas as pd
import numpy as np
import os, random

def Simulador_Ventas():
    print("SIMULADOR DE VENTAS")
    num_clientes = int(input("Para comenzar, Cuántos Clientes desea?\nConsidere a lo menos 50: ")) # Numero de clientes
    num_ventas = int(input("Cuántas ventas desea evaluar?\nConsidere a lo menos 100: "))
    
    while(True):  #mientras las filas sean menor a 50
        if num_clientes < 50 :
            print("Para que el analisis sea mas eficiente considere a lo menos 50 clientes")
            num_clientes = int(input("Cuántos clientes desea?:")) #volver a ingresar numero de filas
        else:
            clientes = DataGen_Clientes(num_clientes)
            FileWrite('clientes.csv', clientes)
                 
            if num_ventas < 100 :
                print("Para que el analisis sea mas eficiente considere a lo menos 100 ventas")
                num_ventas = int(input("Cuántos ventas desea evaluar?:")) #volver a ingresar numero de filas
            else:
                ventas = DataGen_Ventas(num_ventas, clientes)
                FileWrite('ventas.csv',ventas)
                break

def DataGen_Clientes(num_clientes):
    try:
        nombres = NameListGen(num_clientes)
        edad = range(18,80) #Generacion de Edad entre los 18 y 80 años
        genero = ['Femenino','Masculino','Otro']
        ubicacion = ['Norte','Sur','Este','Oeste']
        clientes = pd.DataFrame({
            "ID_Cliente": np.arange(1, num_clientes +1),
            "Nombre": [random.choices(nombres) if random.random() > 0.05 else "NULL" for i in range(num_clientes)],
            "Edad": [random.choices(edad) if random.random() > 0.05 else "NULL" for i in range(num_clientes)],
            "Genero": [random.choice(genero) for i in range(num_clientes)],
            "Ubicacion": [random.choice(ubicacion)for i in range(num_clientes)]
        })
        print(clientes)
    except:
        raise Exception("Ha surgido un error en la generacion de clientes")

def DataGen_Ventas(num_ventas, clientes):
    #region Generacion de datos de ventas
    categoria_aleatoria = list(ProductList().keys())#Seleccionar una categoría aleatoria
    productos_categoria = ProductList()[categoria_aleatoria]["Productos"]#Obtener la lista de productos de la categoría aleatoria
    producto_aleatorio = list(productos_categoria.keys())#Seleccionar un producto aleatorio de la categoría
    precio_producto = productos_categoria[producto_aleatorio]["Precio"]#Obtener el precio del producto aleatorio
    lista_clientes = list(clientes['ID_Cliente'])
    #endregion
    try:
         ventas = pd.DataFrame({
             "ID_Venta": np.arange(1, num_ventas +1),
             "ID_Cliente": [random.choice(lista_clientes) for i in range(num_ventas)],
             "Categoría": [random.choice(categoria_aleatoria) for i in range(num_ventas)],
             "Producto": [random.choice(producto_aleatorio) if random.random() > 0.1 else "NULL" for i in range(num_ventas)],
             "Precio": [precio_producto for i in range(num_ventas)],
             "Cantidad": [np.random.randint(1, 5, size=num_ventas)]
         })
         print(ventas)
         return ventas
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
        print("Ha surgido un error escribiendo el archivo")

#region INTERNAL
def NameListGen(clientes):
    fake = Faker()
    nombres_comunes=[]
    for i in range(clientes):
        name = fake.name()
        nombres_comunes.append(name)
    return nombres_comunes
def ProductList():
    categorias_productos = {
            "Hogar": {
            "Productos": {"Refrigerador":{"Precio": 199990},"Estufa Electrica":{"Precio": 129990}, "Lavadora":{"Precio": 164990}, "Horno Electrico":{"Precio": 189990}, "Lámpara":{"Precio": 4990}}},
            "Electrónica": {
            "Productos": {"Televisor":{"Precio": 159990},
            "Laptop":{"Precio": 699990}, "Computadora":{"Precio": 360608}, "Tablet":{"Precio": 179990}, "Telefono":{"Precio": 296404}, "Licuadora":{"Precio": 19990}, "Batidora":{"Precio": 29990}, "Cafetera":{"Precio": 59990}, "Tostadora":{"Precio": 24990}, "Audífonos":{"Precio": 12990}, "Cámara":{"Precio": 60490}}  
          }
        }
    return categorias_productos
#endregion

def main(): #Solo para depuracion
    Simulador_Ventas()

if __name__ == "__main__":
    main()

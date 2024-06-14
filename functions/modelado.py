'''
Autor: Maria Paz Cisternas Pardo
Version: 24.06.09
Contenido:
1. Cruzar los DataFrames de películas y ratings utilizando la columna "ID_Venta" como clave primaria.
2. Calcular el rating promedio de cada película utilizando una Serie de Pandas.
3. Generar una tabla que muestre la cantidad de ventas por Categoria y Precio utilizando las funciones de agregación de Pandas.
4. Identificar los 10 Productos con mayor venta y los 10 productos con promedio más bajo utilizando indexación fancy y slicing en el DataFrame cruzado.
'''

def Modelado():
    #cruce de df
    ventas_promedio = Ventas_Clientes.groupby("producto")["Precio"].size().to_frame(name="cantidad").reset_index()
    
    print()

def Merge_data(ventas,clientes):
    merged_df = ventas.merge(clientes, on='ID_Cliente')
    Ventas_media = merged_df.groupby('Producto')['Precio'].size().to_frame(name="Cantidad").reset_index()


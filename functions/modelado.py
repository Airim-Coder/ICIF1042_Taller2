'''
Autor: Maria Paz Cisternas Pardo
Version: 24.06.09
Contenido:
1. Cruzar los DataFrames de películas y ratings utilizando la columna "ID_Cliente" como clave primaria.
2. Calcular el rating promedio de cada película utilizando una Serie de Pandas.
3. Generar una tabla que muestre la cantidad de ventas por Categoria y Precio utilizando las funciones de agregación de Pandas.
4. Identificar los 10 Productos con mayor venta y los 10 productos con promedio más bajo utilizando indexación fancy y slicing en el DataFrame cruzado.
'''

def Modelado():
    #cruce de df
    ventas_promedio = ventas_promedio.groupby("producto")["Precio"].size().to_frame(name="cantidad").reset_index()
    
    print()

def Merge_data(ventas,clientes):
    merged_df = ventas.merge(clientes, on='ID_Cliente')# Combinar DataFrames
    Ventas_media = merged_df.groupby('Producto')['Precio'].size().to_frame(name="Cantidad").reset_index()# Calcular el promedio de ventas
    productos_mayor_venta = Ventas_media.nlargest(10, 'count') #Tabla de ventas por categoría y precio
    df_combinado_ordenado = merged_df.sort_values(by='Cantidad', ascending=True) #10 productos con mayor venta:
    productos_menor_promedio = df_combinado_ordenado.head(10) #10 productos con menor promedio:


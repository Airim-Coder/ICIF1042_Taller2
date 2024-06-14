'''
Autor: Maria Paz Cisternas Pardo
Version: 24.06.09
Contenido:
1. Cruzar los DataFrames de películas y ratings utilizando la columna "ID_Venta" como clave primaria.
2. Calcular el rating promedio de cada película utilizando una Serie de Pandas.
3. Generar una tabla que muestre la cantidad de ventas por Categoria y Precio utilizando las funciones de agregación de Pandas.
4. Identificar los 10 Productos con mayor venta y los 10 productos con promedio más bajo utilizando indexación fancy y slicing en el DataFrame cruzado.
'''
import datos

def Estadistico_Ventas():
    #cruce de df
    Ventas_Clientes = datos.df_ventas.merge(datos.df_clientes, on="ID_Clientes")
    rating_promedio = Ventas_Clientes.groupby("producto")["Precio"].size().to_frame(name="cantidad").reset_index()
    
    print()

def main(): #Solo para depuracion
    Estadistico_Ventas()

if __name__ == "__main__":
    main()
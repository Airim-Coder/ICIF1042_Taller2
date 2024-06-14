#Generación de visualiazión y archivo excel
'''
Autor: Jonathan Briones Rozas
Version: 09.06.24
Contenido:
8.    Crear una visualización básica con Seaborn que muestre la distribución de edades de
los clientes por género.
9.    Guardar los resultados generados en un archivo Excel.

Python3 -m venv Taller_2
Source Taller_2/bin/actívate
''' #MC 2024.06.14 -> añadi los docstring para que compilara
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd #MC 2024.06.14 -> añadi para la generacion de excel

def Grafico(df_completo): #MC 2024.06.14 -> Lo converti en un metodo para su utilizacion posterior
# Configuración de Seaborn
    sns.set(style="whitegrid")

    # Crear una visualización básica con Seaborn
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_completo, x="Edad", hue="Genero", multiple="stack", kde=True)
    plt.title("Distribución de edades de los clientes por género")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.show()

def Excel(df_completo,promedio_edad_categoria,top_mas_vendidos,top_menos_vendidos): #MC 2024.06.14 -> Lo converti en un metodo para su utilizacion posterior
# Guardar DataFrame cruzado y los cálculos en un archivo Excel
    with pd.ExcelWriter("docs/resultados.xlsx") as writer:#MC 2024.06.14 -> le dije que lo guardara en la carpeta docs
        df_completo.to_excel(writer, sheet_name="Datos_Cruzados", index=False)
        promedio_edad_categoria.to_excel(writer, sheet_name="Promedio_Edad_Categoria", index=False)
        top_mas_vendidos.to_excel(writer, sheet_name="Top_10_Mas_Vendidos", index=False) #MC 2024.06.14 -> cambie a una variable más descripctiva
        top_menos_vendidos.to_excel(writer, sheet_name="Top_10_Menos_Vendidos", index=False) #MC 2024.06.14 -> cambie a una variable más descripctiva

def main(): #Solo para depuración
    #Simulador_Ventas() #MC 2024.06.14 -> no existe este metodo en la clase
    print("Haz algo de magia")

if __name__ == "__main__":
    main()
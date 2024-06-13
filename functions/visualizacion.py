#Generación de visualiazión y archivo excel
Autor: Jonathan Briones Rozas
Version: 09.06.24
Contenido:
8.    Crear una visualización básica con Seaborn que muestre la distribución de edades de
los clientes por género.
9.    Guardar los resultados generados en un archivo Excel.

Python3 -m venv Taller_2
Source Taller_2/bin/actívate

import seaborn as sns
import matplotlib.pyplot as plt

# Configuración de Seaborn
sns.set(style="whitegrid")

# Crear una visualización básica con Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=df_completo, x="Edad", hue="Genero", multiple="stack", kde=True)
plt.title("Distribución de edades de los clientes por género")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

# Guardar DataFrame cruzado y los cálculos en un archivo Excel
with pd.ExcelWriter("resultados.xlsx") as writer:
    df_completo.to_excel(writer, sheet_name="Datos_Cruzados", index=False)
    promedio_edad_categoria.to_excel(writer, sheet_name="Promedio_Edad_Categoria", index=False)
    top_5_mas_vendidos.to_excel(writer, sheet_name="Top_5_Mas_Vendidos", index=False)
    top_5_menos_vendidos.to_excel(writer, sheet_name="Top_5_Menos_Vendidos", index=False)

def main(): #Solo para depuración
    Simulador_Ventas()

if __name__ == "__main__":
    main()
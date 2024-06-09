# Contexto:
Una tienda de electrónica desea realizar un análisis de sus datos de ventas y clientes para obtener información relevante y tomar decisiones estratégicas. Los datos de ventas incluyen información sobre el ID de venta, el ID de cliente, el nombre del producto, la categoría, el precio unitario y la cantidad vendida. Los datos de clientes incluyen información sobre el ID de cliente, el nombre, la edad, el género y la ubicación.

### Objetivos:
Aplicar los conceptos de manipulación y análisis de datos utilizando la biblioteca Pandas de Python para procesar los datos de ventas y clientes de la tienda, cruzarlos y generar informes que respondan a las preguntas planteadas.
## Requerimientos:
1. Generar dos archivos CSV llamados "ventas.csv" y "clientes.csv" que contengan los datos de ventas y clientes, respectivamente. Los datos deben ser generados aleatoriamente utilizando funciones de probabilidad para simular escenarios realistas (indique en su informe que distribución uso: uniforme, normal u otra). Ejemplo de las primeras líneas de los archivos CSV:
- "ventas.csv":
```
ID_Venta,ID_Cliente,Producto,Categoría,Precio,Cantidad
 1,101,Televisor,Electrónica,500.0,2
 2,102,Lavadora,Hogar,800.0,1
 3,101,NULL,Electrónica,1200.0,1
```
- "clientes.csv":
```
ID_Cliente,Nombre,Edad,Género,Ubicación
 101,Juan Pérez,NULL,Masculino,Norte
 102,María González,35,Femenino,Sur
 103,NULL,28,Masculino,Este
```
Los valores nulos deben representarse con la palabra "NULL". En el archivo "ventas.csv", la columna "Producto" puede contener hasta un 10% de valores nulos. En el archivo "clientes.csv", las columnas "Nombre" y "Edad" pueden contener hasta un 5% de valores nulos cada una.

2. Cargar los datos de ventas y clientes desde los archivos CSV generados utilizando Pandas y almacenarlos en DataFrames separados.

3. Realizar una limpieza de datos inicial en ambos DataFrames, manejando los valores nulos y convirtiendo los tipos de datos según sea necesario. Documentar en el informe los pasos realizados para la limpieza de datos.
Realizar una limpieza de datos inicial en ambos DataFrames, manejando los valores nulos y convirtiendo los tipos de datos según sea necesario. Documentar en el informe los pasos realizados para la limpieza de datos.

4. Cruzar los DataFrames de películas y ratings utilizando la columna "ID_Pelicula" como clave primaria.

5. Calcular el rating promedio de cada película utilizando una Serie de Pandas.

6. Generar una tabla que muestre la cantidad de películas por género y año de lanzamiento
utilizando las funciones de agregación de Pandas.

7. Identificar las 10 películas con el rating promedio más alto y las 10 películas con el
rating promedio más bajo utilizando indexación fancy y slicing en el DataFrame
cruzado.

8. Crear una visualización básica con Seaborn que muestre la distribución de los ratings
por género de película.

9. Guardar los resultados generados en un archivo Excel.

# Rubrica
1. Generación correcta de los archivos CSV con datos aleatorios (15 puntos)
- Creación de los dos archivos CSV requeridos (5 puntos)
- Inclusión de las columnas especificadas en cada archivo (5 puntos)
- Generación de datos aleatorios utilizando funciones de probabilidad (5 puntos)

2. Carga correcta de los archivos CSV y almacenamiento en DataFrames (10 puntos)
- Carga de los datos desde los archivos CSV utilizando Pandas (5 puntos)
- Almacenamiento de los datos en DataFrames separados (5 puntos)

3. Limpieza de datos y manejo de valores nulos (15 puntos)
- Identificación y manejo adecuado de los valores nulos (5 puntos)
- Conversión de los tipos de datos según sea necesario (5 puntos)
- Documentación de los pasos realizados para la limpieza de datos (5 puntos)

4. Cruce correcto de los DataFrames utilizando la clave primaria (10 puntos)
- Identificación de la columna clave primaria (5 puntos)
- Realización del cruce de los DataFrames utilizando la función adecuada (5
puntos)

5. Cálculos y análisis utilizando Pandas (20 puntos)
- Aplicación de las funciones de agregación y transformación de Pandas (10 puntos)
- Generación de tablas y resúmenes estadísticos (5 puntos)
- Utilización correcta de indexación fancy y slicing en los DataFrames (5 puntos)

6. Creación de visualizaciones básicas con Seaborn (10 puntos)
- Selección adecuada del tipo de gráfico según los datos (5 puntos)
- Configuración y personalización de la visualización (5 puntos)

7. Guardado de los resultados en un archivo Excel (5 puntos)
- Exportación de los resultados generados a un archivo Excel (5 puntos)

8. Claridad, estructura y documentación del código (15 puntos)
- Organización y legibilidad del código (5 puntos)
- Uso de comentarios y docstrings para explicar el propósito del código (5 puntos)
- Documentación adecuada de las funciones y clases utilizadas (5 puntos)

9. Calidad del informe y presentación de los resultados (20 puntos)
- Estructura y organización del informe (5 puntos)
- Explicación clara de los pasos realizados y las decisiones tomadas (5 puntos)
- Presentación de los resultados y visualizaciones (5 puntos)
- Conclusiones y recomendaciones basadas en los análisis realizados (5 puntos)

10. Envío del archivo zip con el formato solicitado (5 puntos)
- Creación de un archivo zip que incluya el informe en formato PDF y los archivos
de código (3 puntos) 
- Nombre del archivo zip siguiendo el formato especificado: Tarea_2_Apellido_Nombre.zip (2 puntos)


11. Envío del correo electrónico con el asunto solicitado (5 puntos)
- Envío del archivo zip por correo electrónico a la dirección especificada (3 puntos) b. Asunto del correo electrónico siguiendo el formato: Tarea 2 - Apellido Nombre (2 puntos)

12. Bonus: Implementación de técnicas o análisis adicionales (5 puntos extra)
- Aplicación de técnicas o análisis adicionales más allá de los requerimientos básicos (5 puntos extra)

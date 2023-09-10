### Conversor de Excel a CSV en Python

¡Hola! Soy globosc, y me apasiona trabajar con Python, data, cloud y kubernetes. Recientemente, he desarrollado una herramienta en Python que simplifica la conversión de archivos Excel a archivos CSV. Esto, porque a veces, cuando estás trabajando con windows, al guardar un archivo Excel(.xlsx) a CSV(.csv) no queda bien, se ve como si fuera un archivo tabulado separado por celdas normal y no como uno separado por comas. Es por esto, que usando Python, te ahorras de subir tu archivo a la web, y puedes manejarlo localmente. 

#### Descripción

Este script de Python utiliza la biblioteca `pandas` para abrir un archivo Excel (.xlsx) y convertirlo en un archivo CSV. Es una solución práctica para aquellos que necesitan transformar datos de hojas de cálculo en un formato más accesible y ampliamente compatible.

#### Características

- Convierte archivos Excel (.xlsx) en archivos CSV.
- Fácil de usar desde la línea de comandos.
- Compatible con diferentes versiones de Excel.

#### Uso

Puedes usar este script de la siguiente manera:

```shell
python convert_excel_to_csv.py archivo.xlsx archivo.csv

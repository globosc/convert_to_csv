import pandas as pd
import sys

def convert_excel_to_csv(input_excel, output_csv):
    try:
        # Cargar el archivo Excel en un DataFrame de pandas
        df = pd.read_excel(input_excel)
        
        # Guardar el DataFrame en un archivo CSV
        df.to_csv(output_csv, index=False, encoding='utf-8')
        
        print(f'Se ha convertido {input_excel} a {output_csv} correctamente.')
    except FileNotFoundError:
        print(f'No se pudo encontrar el archivo {input_excel}. Asegúrate de que el archivo exista.')
    except Exception as e:
        print(f'Se produjo un error al convertir el archivo: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python convert_excel_to_csv.py <archivo_excel> <archivo_csv>")
    else:
        input_excel = sys.argv[1]
        output_csv = sys.argv[2]
        convert_excel_to_csv(input_excel, output_csv)

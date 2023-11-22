
import pandas as pd

# Reemplaza 'PLANILLA.XLS' con la ruta completa de tu archivo Excel si no esta en el mismo directorio.
archivo_excel = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\PROCESO\\planillaPy.xlsx'

# Carga el archivo Excel en un DataFrame
df = pd.read_excel(archivo_excel, sheet_name='TOTAL')

# Muestra las primeras 10 filas con las columnas "PARCIALIDAD" y "ESTATUS DOCUMENTO"
primeras_10_filas = df[['PARCIALIDAD', 'ESTATUS']].head(10)

print(primeras_10_filas)

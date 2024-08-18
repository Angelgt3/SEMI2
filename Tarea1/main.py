import csv
import re

def limpiar_datos(nombre_archivo, archivo_salida):
    datos_limpios = []
    
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            # Remover espacios en blanco en cada campo
            fila = {clave: valor.strip() if isinstance(valor, str) else valor for clave, valor in fila.items()}
            
            # Remover caracteres especiales
            fila = {clave: re.sub(r'[^a-zA-Z0-9\s]', '', valor) if isinstance(valor, str) else valor for clave, valor in fila.items()}
            
            # Filtrar filas con valores nulos en columnas críticas
            if all(fila[clave] for clave in ['year', 'unitid', 'institution_name', 'ef_male_count', 'ef_female_count']):
                datos_limpios.append(fila)
    
    # Guardar los datos limpios en un nuevo archivo
    with open(archivo_salida, 'w', newline='') as archivo:
        campos = datos_limpios[0].keys() if datos_limpios else []
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos_limpios)
    
    print(f"Datos limpios guardados en: {archivo_salida}")

# Ejemplo de uso
nombre_archivo = 'C:\\Users\\angge\\OneDrive\\Escritorio\\archive\\datos.csv'
archivo_salida = 'C:\\Users\\angge\\OneDrive\\Escritorio\\archive\\datos_limpios.csv'
limpiar_datos(nombre_archivo, archivo_salida)

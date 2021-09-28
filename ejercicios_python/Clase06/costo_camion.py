"""
El programa costo_camion.py lee, mediante una función llamada costo_camion() los datos de un camión y calcula su costo.
- Modifica el archivo costo_camion.py para que use la función informe_funciones.leer_camion() del programa informe_funciones.py.
"""

from informe_funciones import leer_camion

def costo_camion(nombre_archivo):
    """
    Devuelve el costo total del camion
    """
    camion = leer_camion(nombre_archivo)
    costo_total = 0
    for item in camion:
        costo_total += item['cajones'] * item['precio']
    return costo_total
        
print(f"El costo total es ${costo_camion('../Data/camion.csv')}")
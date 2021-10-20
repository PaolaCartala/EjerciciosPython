#! python3

"""
Modificá la función leer_camion() de modo que cree una instancia de Camion.
Para ejecutarlo en el símbolo del sistema (Windows) tenes que posicionarte en la carpeta Clase10 y correr la línea.
Formato txt predeterminado:
> python informe_final.py ../Data/camion.csv ../Data/precios.csv
Formato csv:
> python informe_final.py ../Data/camion.csv ../Data/precios.csv csv
Formato html:
> python informe_final.py ../Data/camion.csv ../Data/precios.csv html

"""
#%%
import sys
import fileparse
import lote
import formato_tabla
from camion import Camion

#%%
def leer_camion(nombre_archivo):
    """
    Devuelve una lista de diccionarios con [{'nombre', 'cajones', 'precio'}] de cada item del archivo
    """
    with open(nombre_archivo) as file:
        camion_dicts = fileparse.parse_csv(file, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return Camion(camion)

#%%
def leer_precios(nombre_archivo):
    """
    Devuelve un diccionario {'nombre':'precio'} de cada item del archivo de precios al consumidor
    """
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(lista_cajones, precios):
    """
    Devuelve una lista de tuplas con el nombre del item, la cantidad de cajones en enteros, su precio de costo en punto flotante y la diferencia entre el costo y el precio de venta en punto flotante
    """
    informe = []
    camion = []
    [camion.append({'nombre': item.nombre, 'cajones': item.cajones, 'precio': item.precio}) for item in lista_cajones]
    for p in camion:
        for f in precios:
            if f == p['nombre']:
                p['cambio'] = precios[f] - p['precio']
                informe.append(tuple(p.values()))
    return informe

def imprimir_informe(informe, formateador):
    """
    Imprime una tabla (informe) con el nombre de cada item, la cantidad de cajones, su precio unitario y la ganancia
    """
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    """
    Crea una función de alto nivel que ejecuta las funciones anteriores en un solo llamado.
    El formato predeterminado de la salida es txt, alternativas: csv o html
    """
    # Datos para el informe
    datos_camion = leer_camion(nombre_archivo_camion)
    precios_venta = dict(leer_precios(nombre_archivo_precios))
    informe = hacer_informe(datos_camion, precios_venta)
    # Imprimirlo con el formateador nuevo
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)

def f_principal(argv):
    try:
        informe_camion(argv[1], argv[2], argv[3])
    except IndexError:
        informe_camion(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)

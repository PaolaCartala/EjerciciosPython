"""
Creá un archivo nuevo llamado formato_tabla.py y definí la clase FormatoTabla. La clase FormatoTabla es sólo la base de un sistema extensible. Éste es el momento de extenderla.
Definí una clase FormatoTablaTXT.
Definí una nueva clase llamada FormatoTablaCSV que genere la salida en formato CSV.
Usando las mismas ideas creá la clase FormatoTablaHTML.
Agregá la función crear_formateador(nombre) que permita crear un objeto formateador dado un tipo de salida como txt, csv, o html.
Creá una función imprimir_tabla() usando la función getattr() que imprima una tabla mostrando, de una lista de objetos de tipo arbitrario, una lista de atributos especificados por le usuarie, imprimir_tabla() también debería aceptar cualquier instancia de la clase FormatoTabla para definir el formato de la salida.
"""

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h.capitalize():>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print(f'<tr>', end=' ')
        for h in headers:
            print(f'<th>{h:>10s}</th>', end=' ')
        print(f'</tr>')

    def fila(self, data_fila):
        print(f'<tr>', end=' ')
        for d in data_fila:
            print(f'<td>{d:>10s}</td>', end=' ')
        print(f'</tr>')

def crear_formateador(nombre):
    """
    Devuelve el formateador según la eleccion del usuario
    """
    if nombre == 'txt':
        formateador = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {nombre}')
    return formateador

def imprimir_tabla(archivo, columnas, formateador):
    """
    Muestra una tabla con el fomrato pasado por el formateador, con las columnas seleccionadas del archivo
    """
    formateador.encabezado(columnas) # pasamos el encabezado, una lista
    for item in archivo: # por cada item del archivo
        atributos = []
        for columna in columnas: # y por cada columna del encabezado
            atributos.append(str(getattr(item, columna))) # obtenemos cada atributo como string, y lo agregamos a la lista de atributos
        formateador.fila(atributos) # a esa lista de atributos la mandamos como fila al formateador
"""
Escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio de determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.
"""

def buscar_precio(fruta):
    """
    Busca en el archivo ../Data/precios.csv el valor pasado en el parámetro fruta e imprime su precio, si no se encuentra en el archivo muestra un mensaje
    """
    f = open('../Data/precios.csv', 'rt')
    productos = ""
    for i in f:
        item = i.split(',')
        productos += f"{item[0]} "
        for p in item:
            if p == fruta:
                precio = item[-1]
                print(f"El precio de la {fruta} es: ${precio}")
    if fruta not in productos:
        print(f"{fruta} no figura en el listado de precios")

buscar_precio("Frambuesa")
buscar_precio("Kale")
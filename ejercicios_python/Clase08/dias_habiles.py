"""
Escribí una función dias_habiles(inicio, fin, feriados) que calcule los días hábiles entre dos fechas dadas. La función debe tener como argumentos el día inicial, el día final, y una lista con las fechas correspondientes a los feriados que haya en ese lapso, y debe devolver una lista con las fechas de días hábiles del período, incluyendo la fecha inicial y la fecha final indicadas. Las fechas de entrada y salida deben manejarse en formato de texto
"""
from datetime import date, datetime, timedelta
from busqueda_en_listas import busqueda_binaria

def dias_habiles(inicio, fin, feriados):
    """
    Calcula los días hábiles entre las fechas inicio y fin en formato dd/m/AAAA, quitando los feriados de la lista de strings feriados (con fechas del mismo formato)
    """
    habiles = []
    inicio = datetime.strptime(inicio, '%d/%m/%Y')
    fin = datetime.strptime(fin, '%d/%m/%Y')
    diferencia = fin - inicio
    for i in range(diferencia.days + 1):
        dia = inicio + timedelta(days=i)
        if date.weekday(dia) != 5 and date.weekday(dia) != 6: # primero agrega a la lista los días de lunes a viernes
            habil = dia.strftime('%Y/%m/%d')
            habiles.append(habil)
    for f in feriados:
        feriado = datetime.strptime(f, '%d/%m/%Y').strftime('%Y/%m/%d')
        if busqueda_binaria(habiles, feriado)[0] != -1: # busca entre los lunes a viernes si alguno es feriado y lo elimina de la lista de días habiles
            habiles.remove(feriado)
    return habiles

feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
dias_habiles('20/9/2020', '10/10/2020', feriados)
dias_habiles('20/9/2020', '31/12/2020', feriados)
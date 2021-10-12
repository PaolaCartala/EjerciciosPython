"""
Escribí una función llamada vida_en_segundos(fecha_nac) a la que le pasás tu fecha de nacimiento y te devuelve la cantidad de segundos que viviste (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento). La función debe tomar como entrada una cadena en formato 'dd/mm/AAAA' (día, mes, año con 2, 2 y 4 dígitos, separados con barras normales) y devolver un float.
"""
from datetime import datetime

def vida_en_segundos(fecha_nac):
    """
    Retorna la cantidad de segundos vividos desde la fecha de nacimiento hasta la hora actual
    """
    nacimiento = datetime.strptime(fecha_nac, '%d/%m/%Y')
    hoy = datetime.now()
    vida = hoy - nacimiento
    return vida.total_seconds()

vida_en_segundos('23/01/1991')
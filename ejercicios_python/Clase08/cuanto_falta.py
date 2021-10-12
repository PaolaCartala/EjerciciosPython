"""
Un conocido canal Argentino tiene por costumbre anunciar la cantidad de días que faltan para la próxima primavera. Escribí un programa que asista a los técnicos del canal indicándoles, al correr el programa el número que deben poner en la placa.
"""
from datetime import date

def cuanto_falta():
    """
    Retorna la cantidad de días que faltan para el siguiente inicio de la primavera
    """
    primavera = date(year = 2022, month = 9, day = 21)
    hoy = date.today()
    dias = primavera - hoy
    return dias.days

cuanto_falta()
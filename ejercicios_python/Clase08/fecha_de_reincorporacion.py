"""
Si tenés una licencia por xaternidad que empieza el 26 de septiembre de 2020 y dura 200 días, ¿qué día te reincorporás al trabajo?
"""

from datetime import date, timedelta

fecha = date(year = 2020, month = 9, day = 26)
licencia = timedelta(days = 200)
reincorporacion = fecha + licencia
print(f'La reincorporación de la licencia debe ser en la fecha: {reincorporacion}')
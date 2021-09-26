"""
David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.
- Calcula el monto total que pagará David a lo largo de los años
- Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca. Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos
- ¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?
- Modificá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante
- Corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.
"""

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    meses += 1
    if saldo < pago_mensual:
        pago_mensual = saldo * (1+tasa/12)
    print(f"Cuota {meses}\n Saldo: ${round(saldo, 2)}, Total pagado: ${round(total_pagado, 2)}")
    if meses >= pago_extra_mes_comienzo and meses <= pago_extra_mes_fin :
        total_pagado += pago_extra
        saldo -= pago_extra

print('Total pagado $', round(total_pagado, 2))
print(f'Meses: {meses}')
"""
Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó.
"""
altura = 100
for i in range(1,11):
    altura = altura * (3/5)
    print(f"{i} rebote, {round(altura, 2)}")

# -*- coding: utf-8 -*-
"""
animal.py
"""
#%%
import random

#%%
class Animal(object):
    """docstring for Animal"""
    def __init__(self):
        super(Animal, self).__init__()
        self.reproducciones_pendientes = 4
        self.edad = 0
        self.sexo = None # Posible mejora para que no se puedan reproducir dos del mismo sexo
        self.energia = self.energia_maxima
        self.es_reproductore = False

    def pasar_un_ciclo(self):
        self.energia -= 1 # Se puede restar si no llega a comer
        self.edad += 1
        if self.reproducciones_pendientes > 0 and self.edad >= 2 and self.energia > 4: #
            self.es_reproductore = True

    def en_vida(self):
        return (self.edad <= self.edad_maxima) and self.energia > 0

    def tiene_hambre(self):
        """Acá se puede poner comportamiento para que no tenga hambre todo el tiempo
        debería depender de la diferencia entre su nivel de energía y su energía máxima"""
        if self.energia <= 5:
            return True
        else:
            return False
        #pass

    def es_leon(self):
        return False

    def es_antilope(self):
        return False

    def puede_reproducir(self):
        return self.es_reproductore

    def tener_cria(self):
        """Acá se puede poner comportamiento que sucede al tener cria para evitar que tenga más de una cria por ciclo, etc"""
        self.reproducciones_pendientes -= 1
        self.energia -= 2 # tener una cria resta 2 de energía
        # pass

    def reproducirse(self, vecinos, lugares_libres):
        pos = None
        if vecinos:
            for vecino in vecinos:
                if (self.es_leon() and vecino.es_leon() and lugares_libres) or (self.es_antilope() and vecino.es_antilope() and lugares_libres): # verifica si las parejas son de la misma especie
                    pareja = vecino
                    # pareja = random.choice(vecinos)
                    if (self.edad >= 2 and pareja.edad >= 2) and (self.energia > 4 and pareja.energia > 4): # agrega el condicionante de que las parejas tengan más de 2 años y tengan más de 4 de energía para no tener más de una cria por ciclo dado que resta 2 de energia
                        self.tener_cria()
                        pareja.tener_cria()
                        pos = random.choice(lugares_libres)
                        break

        return pos

    def alimentarse(self, animales_vecinos = None):
        self.energia = self.energia_maxima
        return None

    def moverse(self, lugares_libres):
        pos = None
        if lugares_libres:
            pos = random.choice(lugares_libres)

        return pos

    def fila_str(self):
        return f"{self.edad:>3d}    {self.energia:>3d}/{self.energia_maxima:<3d}       {self.es_reproductore!s:<5}"

    def __format__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()

#%%
class Leon(Animal):
    """docstring for Leon"""
    def __init__(self):
        self.energia_maxima = 6
        self.edad_maxima = 10
        super(Leon, self).__init__()

    def es_leon(self):
        return True

    def alimentarse(self, animales_vecinos):
        # Se alimenta si puede e indica la posición del animal que se pudo comer
        pos = None
        if self.tiene_hambre(): # no está lleno
            presas_cercanas = [ (pos,animal) for (pos, animal) in animales_vecinos if animal.es_antilope() ]
            if presas_cercanas: # y hay presas cerca
                super(Leon, self).alimentarse()
                (pos, animal) = random.choice(presas_cercanas)

        return pos


    def __repr__(self):
        # return "León"
        return "L{}".format(self.edad)


#%%
class Antilope(Animal):
    """docstring for Antilope"""
    def __init__(self):
        self.energia_maxima = 10
        self.edad_maxima = 6
        super(Antilope, self).__init__()
        self.reproducciones_pendientes = 3

    def es_antilope(self):
        return True

    def __repr__(self):
        # return "A"
        return "A{}".format(self.edad)


# %%
"""
# agregamos un leon
L = Leon()
L.energia
L.edad
L.es_leon()
L.es_antilope()
L.pasar_un_ciclo()
L.energia
L.edad
L.tiene_hambre()

#%%
# agregamos dos antilopes
A1 = Antilope()
A2 = Antilope()
A1.energia
A1.edad
A1.es_antilope()

# %%
# el leon se come alguno de los antilopes
vecinos = [(1,A1),(2,A2)]
pos = L.alimentarse(vecinos)
if pos:
    print(f'El león se come al antílope A{pos}')
else:
    print(f'El león no come')

# %%
# leona m y hacemos que pasen unos ciclos hasta que sea reproductora
M = Leon()
M.puede_reproducir()
M.pasar_un_ciclo()
M.puede_reproducir()

#%%
# Digamos que M tiene como vecinos a los dos antílopes y al león L de antes. Supongamos que las crias pueden ocupar algunos lugares libres en nuestro mundo
vecinos = [L]
lugares_libres = [4,5,6,7,8]
L.puede_reproducir()
M.puede_reproducir()

pos = M.reproducirse(vecinos, lugares_libres)
print(f'nace un nuevo leoncito en la posición {pos}')
M.puede_reproducir()
M.pasar_un_ciclo()
M.puede_reproducir()
"""
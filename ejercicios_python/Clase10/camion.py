"""
En un nuevo archivo llamado camion.py, definí la clase Camion con los métodos precio_total() y contar_cajones().
Modificá la clase Camion y hacela iterable.
Probá modificar la clase Camion de modo que tenga algunos de los métodos que vimos en la Clase 9:
- Definí __contains__
- Agregá más métodos especiales (__len__ y __getitem__)
- Por último, agregale los métodos __repr__ y __str__
Hiciste algunos cálculos usando comprensión de listas, reemplazá esas expresiones por expresiones generadoras.
"""
#%%
class Camion:

    def __init__(self, lotes):
        self.lotes = lotes
    
    def __iter__(self):
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self, index):
        return self.lotes[index]
    
    def __str__(self):
        print(f'Camion con {self.__len__()} lotes:')
        contenido = ''
        for item in self.lotes:
            contenido += f'Lote de {item.cajones} de {item.nombre}, pagados a ${item.precio} cada uno.\n'
        return contenido
    
    def __repr__(self) -> str:
        return f'Camion({self.lotes})'

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total

# %%

"""

"""
#%%
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    # def __iter__(self):
    #     return self.__iter__()
    
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, cantidad):
        self.cajones -= cantidad
    
    def __repr__(self) -> str:
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"


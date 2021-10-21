"""
Definí una clase llamada Lote que represente un lote de cajones de una misma fruta. Definila de modo que cada instancia de la clase Lote (es decir, cada objeto lote) tenga los atributos nombre, cajones, y precio.
Modificá el objeto Lote de modo que el método __repr__() genere una salida más agradable.
"""
#%%
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, cantidad):
        self.cajones -= cantidad
    
    def __repr__(self) -> str:
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"


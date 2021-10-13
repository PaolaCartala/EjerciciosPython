"""
Escribí una definición de una clase Canguro que tenga:
- Un método __init__ que recibe un nombre para el canguro y una lista (parámetro opcional) e inicializa un atributo llamado contenido_marsupio con la lista que le pases como parámetro o como lista vacía si no le pasás nada.
- Un método llamado meter_en_marsupio que, dado un objeto cualquiera, lo agregue a la lista contenido_marsupio.
- Un método __str__ que devuelve una representación como cadena del objeto Canguro indicando su nombre y los contenidos de su marsupio.
Luego, mirá el ejemplo canguro_malo copiado a continuación. Este ejemplo intenta resolver el problema anterior, pero tiene un bug. Analizalo y corregilo.
"""
#%%

class Canguro:
    def __init__(self, nombre, contenido_marsupio = None):
        """
        Inicializa el Canguro, nombre es un string y contenido_marsupio es una lista opcional de contenido en el marsupio.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido_marsupio

    def meter_en_marsupio(self, objeto):
        """
        Agrega objetos en el marsupio.
        """
        self.contenido_marsupio.append(objeto)
    
    def __str__(self) -> str:
        """
        Devuelve un string con el nombre del canguro y el contenido de su marsupio.
        """
        contenido = f'Canguro {self.nombre} tiene en su marsupio: '
        for item in self.contenido_marsupio:
            contenido += f'\n{object.__str__(item)}'
        return contenido

#%%
# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=None): # contenido=[] estaba guardando las modificaciones al ser mutable, lo cambié por un tipo inmutable y lo inicializo en la función
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        if contenido is None:
            contenido = []
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.

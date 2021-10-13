"""
Creá una clase llamada Rectangulo que va a estar definido por dos puntos. Para esos dos puntos, usá la clase Punto. El rectángulo es paralelo a los ejes, los puntos representan dos esquinas opuestas cualesquiera. La clase debe tener un método constructor para crear el rectángulo a partir de dos puntos y los siguientes métodos: 
- base() que dé la medida de la base del rectángulo. 
- altura() que dé la medida de la altura del rectángulo. 
- area() que dé la medida del área del rectángulo. 
- Creá métodos especiales __str__ y __repr__.
- desplazar(desplazamiento) que dado un desplazamiento (de tipo Punto) desplace el rectángulo en ambas coordenadas usando el método add de la clase Punto.
- rotar() que rote el rectángulo sobre su esquina inferior derecha 90 grados a la derecha.
"""

#%%
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)

#%%
class Rectangulo(Punto):
    def __init__(self, punto1, punto2):
        """
        Crea un rectángulo a partir de dos puntos
        """
        self.punto1 = punto1
        self.punto2 = punto2
    
    def base(self):
        """
        Da la medida de la base del rectángulo.
        """
        return abs(self.punto2.x - self.punto1.x)
    
    def altura(self):
        """
        Da la medida de la altura del rectángulo.
        """
        return abs(self.punto1.y - self.punto2.y)
    
    def area(self):
        """
        Da la medida del área del rectángulo.
        """
        return self.base() * self.altura()
    
    def __str__(self):
        return f'Rectángulo(I({self.punto1.x},{self.punto1.y}), II({self.punto2.x}, {self.punto1.x}), III({self.punto2.x}, {self.punto2.y}), IV({self.punto1.x}, {self.punto2.y})'
    
    def __repr__(self):
        return f'Rectangulo(Punto({self.punto1.x}, {self.punto1.y}), Punto({self.punto2.x}, {self.punto2.y}))'
    
    def desplazar(self, desplazamiento):
        """
        Dado un desplazamiento de tipo Punto desplaza el rectángulo en ambas coordenadas.
        """
        self.punto1 = self.punto1.__add__(desplazamiento)
        self.punto2 = self.punto2.__add__(desplazamiento)
    
    def rotar(self):
        """
        Rota el rectángulo sobre su esquina inferior derecha 90 grados a la derecha.
        """
        self.punto1.x = self.punto2.x + self.altura()
        self.punto1.y = self.punto2.x

#%%
ul = Punto(0,2)
lr = Punto(1,0)
ll = Punto(0,0)
ur = Punto(1,2)

#%%
rect1 = Rectangulo(ul,lr)
rect2 = Rectangulo(ll,ur)

"""
Usando un par de objetos de la clase Cola, escribí una nueva clase llamada TorreDeControl que modele el trabajo de una torre de control de un aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen prioridad sobre los que están esperando para despegar.
"""

#%%
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

#%%
class TorreDeControl(Cola):
    def __init__(self):
        self.items = []
        self.items_con_prioridad = []

    def nuevo_arribo(self, avion):
        """
        Agrega a la lista de espera al avión que quiere aterrizar, con prioridad.
        """
        self.items_con_prioridad.append(avion)

    def nueva_partida(self, avion):
        """
        Agrega a la lista de espera al avión que quiere despegar, sin prioridad.
        """
        super().encolar(avion)

    def ver_estado(self):
        """
        Muestra el estado de la lista de espera.
        """
        print(f'Vuelos esperando para aterrizar: {self.items_con_prioridad}')
        print(f'Vuelos esperando para despegar: {self.items}')

    def asignar_pista(self):
        """
        Asigna la pista tanto para el aterrizaje como para el despegue según prioridad.
        """
        if len(self.items_con_prioridad) != 0:
            return print(f'El vuelo {self.items_con_prioridad.pop(0)} aterrizó con éxito.')
        elif len(self.items) != 0:
            return print(f'El vuelo {super().desencolar()} despegó con éxito.')
        if len(self.items_con_prioridad) == 0 and super().esta_vacia():
            return print('No hay vuelos en espera.')


#%%
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()

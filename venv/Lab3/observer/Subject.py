#Declara un set de métodos para manejar a los suscriptores
class Subject:
    __observers = []
    __state = 0
    def attach(self, observer):
        self.__observers.append(observer)

    def notifyAllObservers(self, state):
        for observer in self.__observers:
            observer.update(state)

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state
        self.notifyAllObservers(state)
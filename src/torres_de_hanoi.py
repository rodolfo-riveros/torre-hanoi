class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_top(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def ver_pila(self):
        return self.items

class TorresDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.torres = {
            'A': Pila(),
            'B': Pila(),
            'C': Pila()
        }
        self.inicializar()

    def inicializar(self):
        for disco in range(self.num_discos, 0, -1):
            self.torres['A'].apilar(disco)

    def mover(self, origen, destino):
        if not self.torres[origen].esta_vacia() and \
           (self.torres[destino].esta_vacia() or self.torres[destino].ver_top() > self.torres[origen].ver_top()):
            disco = self.torres[origen].desapilar()
            self.torres[destino].apilar(disco)
            return True
        else:
            return False  # Movimiento inválido

    def estado(self):
        return {torre: self.torres[torre].ver_pila() for torre in self.torres}

class HolaMundo:
    def __init__(self):
        self.mensaje = "Hola Mundo"

    def mostrar_mensaje(self):
        print(self.mensaje)

if __name__ == "__main__":
    instancia = HolaMundo()
    instancia.mostrar_mensaje()

import sympy as sp

class Limite:
    """
    Clase para calcular el límite de una función matemática con respecto a una variable en un punto dado.

    Atributos:
        funcion (sympy.Expr): Expresión de sympy que representa la función para la cual se calcula el límite.
        variable (sympy.Symbol): Símbolo de sympy que representa la variable en la expresión.
        destino (numeric | sympy.Symbol): El punto hacia el cual la variable se aproxima.
        direccion (str): La dirección desde la cual se aproxima la variable, '+' por defecto, puede ser '-' para límites desde la izquierda.

    Métodos:
        calcular(): Calcula el límite de la función en el destino desde la dirección dada.
    """

    def __init__(self, funcion, variable, destino, direccion='+'):
        """
        Inicializa la clase Limite con la función, la variable, el punto de destino y la dirección del límite.

        Parámetros:
            funcion (str): Una cadena que representa la función matemática para la cual se calculará el límite.
            variable (str): Una cadena que representa la variable en la expresión de la función.
            destino (numeric | str): El valor o símbolo hacia el cual se aproxima la variable.
            direccion (str, opcional): La dirección desde la cual se aproxima la variable, puede ser '+' para límites desde la derecha (por defecto) o '-' para límites desde la izquierda.
        """
        self.funcion = sp.sympify(funcion)
        self.variable = sp.symbols(variable)
        self.destino = destino if isinstance(destino, sp.Symbol) else sp.sympify(destino)
        self.direccion = direccion

    def calcular(self):
        """
        Calcula el límite de la función dada en el punto de destino desde la dirección especificada.

        Devuelve:
            sympy.Expr: El resultado del cálculo del límite, puede ser un valor numérico o una expresión simbólica.
        """
        return sp.limit(self.funcion, self.variable, self.destino, self.direccion)

# Ejemplo de uso de la clase Limite
if __name__ == "__main__":
    # Ejemplo de cómo crear una instancia de Limite y usarla para calcular un límite
    funcion = "sin(x)/x"
    variable = "x"
    destino = 0
    limite_instancia = Limite(funcion, variable, destino)
    resultado_limite = limite_instancia.calcular()

    print(f"El límite de la función {funcion} cuando {variable} tiende a {destino} es: {resultado_limite}")

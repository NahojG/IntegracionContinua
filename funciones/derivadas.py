import sympy as sp

class Derivada:
    """
    Clase para calcular la derivada de una función matemática con respecto a una variable.

    Atributos:
        funcion (sympy.Expr): Expresión de sympy que representa la función a derivar.
        variable (sympy.Symbol): Símbolo de sympy que representa la variable respecto a la cual derivar.

    Métodos:
        calcular(punto=None): Calcula la derivada de la función. Si se proporciona un punto, evalúa la derivada en ese punto.
    """

    def __init__(self, funcion, variable):
        """
        Inicializa la clase Derivada con la función y la variable proporcionadas.

        Parámetros:
            funcion (str): Una cadena que representa la función matemática a derivar.
            variable (str): Una cadena que representa la variable respecto a la cual derivar.
        """
        self.funcion = sp.sympify(funcion)
        self.variable = sp.symbols(variable)

    def calcular(self, punto=None):
        """
        Calcula la derivada de la función dada. Si se proporciona un punto, también evalúa la derivada en ese punto.

        Parámetros:
            punto (numeric, opcional): El valor de la variable en el que se evaluará la derivada. Por defecto es None.

        Devuelve:
            sympy.Expr: La derivada de la función como una expresión de sympy si no se proporciona un punto,
                        o un valor numérico si se evalúa en un punto dado.
        """
        derivada = sp.diff(self.funcion, self.variable)
        if punto is not None:
            return derivada.subs(self.variable, punto)
        return derivada

# Ejemplo de uso de la clase Derivada
if __name__ == "__main__":
    # Ejemplo de cómo crear una instancia de Derivada y usarla para calcular una derivada
    funcion = "x**2 + 3*x + 1"
    variable = "x"
    derivada_instancia = Derivada(funcion, variable)
    derivada_expr = derivada_instancia.calcular()
    derivada_punto = derivada_instancia.calcular(2)

    print(f"La derivada de la función {funcion} es: {derivada_expr}")
    print(f"El valor de la derivada en el punto x=2 es: {derivada_punto}")

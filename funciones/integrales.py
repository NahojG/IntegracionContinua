import sympy as sp

class Integral:
    """
    Clase para calcular integrales indefinidas y definidas de funciones matemáticas.

    Atributos:
        funcion (sympy.Expr): Expresión de sympy que representa la función a integrar.
        variable (sympy.Symbol): Símbolo de sympy que representa la variable de integración.

    Métodos:
        calcular_indefinida(): Calcula la integral indefinida (antiderivada) de la función.
        calcular_definida(limite_inferior, limite_superior): Calcula la integral definida de la función en el intervalo dado.
    """

    def __init__(self, funcion, variable):
        """
        Inicializa la clase Integral con la función y la variable proporcionadas.

        Parámetros:
            funcion (str): Una cadena que representa la función matemática a integrar.
            variable (str): Una cadena que representa la variable de integración.
        """
        self.funcion = sp.sympify(funcion)
        self.variable = sp.symbols(variable)

    def calcular_indefinida(self):
        """
        Calcula la integral indefinida (antiderivada) de la función dada.

        Devuelve:
            sympy.Expr: La integral indefinida de la función como una expresión de sympy.
        """
        return sp.integrate(self.funcion, self.variable)

    def calcular_definida(self, limite_inferior, limite_superior):
        """
        Calcula la integral definida de la función dada entre dos límites.

        Parámetros:
            limite_inferior (numeric): El límite inferior de integración.
            limite_superior (numeric): El límite superior de integración.

        Devuelve:
            sympy.Expr: El resultado numérico o simbólico de la integral definida.
        """
        return sp.integrate(self.funcion, (self.variable, limite_inferior, limite_superior))

# Ejemplo de uso de la clase Integral
if __name__ == "__main__":
    # Ejemplo de cómo crear una instancia de Integral y usarla para calcular una integral
    funcion = "sin(x)"
    variable = "x"
    integral_instancia = Integral(funcion, variable)
    integral_indefinida = integral_instancia.calcular_indefinida()
    integral_definida = integral_instancia.calcular_definida(0, sp.pi)

    print(f"La integral indefinida de la función {funcion} es: {integral_indefinida}")
    print(f"La integral definida de la función {funcion} entre 0 y pi es: {integral_definida}")

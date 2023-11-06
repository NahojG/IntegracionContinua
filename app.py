# Asumiendo que los módulos derivadas, integrales, limites, y distribucion están en el mismo directorio
from funciones.derivadas import Derivada
from funciones.integrales import Integral
from funciones.limites import Limite
from funciones.distribucion import DistribucionBinomial, DistribucionPoisson, DistribucionNormal
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class CalculadoraMatematica:
    """
    Clase calculadora para realizar cálculos de derivadas, integrales, límites y distribuciones de probabilidad.
    """

    def calcular_derivada(self, funcion, variable, punto=None):
        """
        Calcula la derivada de una función matemática.

        Parámetros:
            funcion (str): La función a derivar.
            variable (str): La variable respecto a la cual se deriva.
            punto (numeric, opcional): El punto en el que se evaluará la derivada.

        Devuelve:
            La derivada de la función como una expresión simbólica o un valor numérico si se proporciona un punto.
        """
        derivada = Derivada(funcion, variable)
        return derivada.calcular(punto)

    def calcular_integral(self, funcion, variable, limite_inferior=None, limite_superior=None):
        """
        Calcula una integral definida o indefinida de una función matemática.

        Parámetros:
            funcion (str): La función a integrar.
            variable (str): La variable de integración.
            limite_inferior (numeric, opcional): El límite inferior de la integral definida.
            limite_superior (numeric, opcional): El límite superior de la integral definida.

        Devuelve:
            La integral de la función como una expresión simbólica o un valor numérico si se proporcionan ambos límites.
        """
        integral = Integral(funcion, variable)
        if limite_inferior is not None and limite_superior is not None:
            return integral.calcular_definida(limite_inferior, limite_superior)
        else:
            return integral.calcular_indefinida()

    def calcular_limite(self, funcion, variable, destino, direccion='+'):
        """
        Calcula el límite de una función matemática cuando la variable se aproxima a un destino desde una dirección dada.

        Parámetros:
            funcion (str): La función para la cual se calculará el límite.
            variable (str): La variable en la expresión de la función.
            destino (numeric | str): El valor hacia el cual se aproxima la variable.
            direccion (str, opcional): La dirección desde la cual se aproxima la variable ('+' por defecto).

        Devuelve:
            El límite de la función como un valor numérico o simbólico.
        """
        limite = Limite(funcion, variable, destino, direccion)
        return limite.calcular()

    def calcular_distribucion_binomial(self, n, p, k):
        """
        Calcula la función de masa de probabilidad y la función de distribución acumulada de una distribución binomial.

        Parámetros:
            n (int): Número de ensayos.
            p (float): Probabilidad de éxito en cada ensayo.
            k (int): Número de éxitos para calcular la probabilidad.

        Devuelve:
            Un diccionario con la PMF y la CDF para k éxitos.
        """
        dist = DistribucionBinomial(n, p)
        return {
            'pmf': dist.pmf(k),
            'cdf': dist.cdf(k)
        }

    def calcular_distribucion_poisson(self, mu, k):
        """
        Calcula la función de masa de probabilidad y la función de distribución acumulada de una distribución de Poisson.

        Parámetros:
            mu (float): La tasa media de ocurrencia en un intervalo dado.
            k (int): Número de ocurrencias para calcular la probabilidad.

        Devuelve:
            Un diccionario con la PMF y la CDF para k ocurrencias.
        """
        dist = DistribucionPoisson(mu)
        return {
            'pmf': dist.pmf(k),
            'cdf': dist.cdf(k)
        }

    def calcular_distribucion_normal(self, mu, sigma, x):
        """
        Calcula la función de densidad de probabilidad y la función de distribución acumulada de una distribución normal.

        Parámetros:
            mu (float): La media de la distribución.
            sigma (float): La desviación estándar de la distribución.
            x (float): El valor para calcular la probabildad.

        Devuelve:
            Un diccionario con la PDF y la CDF para el valor x.
        """
        dist = DistribucionNormal(mu, sigma)
        return {
            'pdf': dist.pdf(x),
            'cdf': dist.cdf(x)
        }
        
calculadora = CalculadoraMatematica()
print(calculadora.calcular_derivada("x^2", "x"))

@app.route('/calcular_derivada', methods=['POST'])
def calcular_derivada_endpoint():
    data = request.json
    resultado = str(calculadora.calcular_derivada(data['funcion'], data['variable'], data.get('punto')))
    return jsonify({'resultado': resultado})

@app.route('/calcular_integral', methods=['POST'])
def calcular_integral_endpoint():
    data = request.json
    resultado = str(calculadora.calcular_integral(data['funcion'], data['variable'], data.get('limite_inferior'), data.get('limite_superior')))
    return jsonify({'resultado': resultado})

@app.route('/calcular_limite', methods=['POST'])
def calcular_limite_endpoint():
    data = request.json
    resultado = calculadora.calcular_limite(data['funcion'], data['variable'], data['destino'], data.get('direccion', '+'))
    return jsonify({'resultado': resultado})

@app.route('/calcular_distribucion_binomial', methods=['POST'])
def calcular_distribucion_binomial_endpoint():
    data = request.json
    resultado = calculadora.calcular_distribucion_binomial(data['n'], data['p'], data['k'])
    return jsonify(resultado)

@app.route('/calcular_distribucion_poisson', methods=['POST'])
def calcular_distribucion_poisson_endpoint():
    data = request.json
    resultado = calculadora.calcular_distribucion_poisson(data['mu'], data['k'])
    return jsonify(resultado)

@app.route('/calcular_distribucion_normal', methods=['POST'])
def calcular_distribucion_normal_endpoint():
    data = request.json
    resultado = calculadora.calcular_distribucion_normal(data['mu'], data['sigma'], data['x'])
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)



from scipy.stats import binom, poisson, norm

class DistribucionBinomial:
    """
    Clase para calcular propiedades y probabilidades de la distribución binomial.
    """

    def __init__(self, n, p):
        """
        Inicializa la distribución binomial con el número de ensayos y la probabilidad de éxito.

        Parámetros:
            n (int): Número de ensayos.
            p (float): Probabilidad de éxito en cada ensayo.
        """
        self.n = n
        self.p = p

    def pmf(self, k):
        """
        Calcula la función de masa de probabilidad para un número dado de éxitos.

        Parámetros:
            k (int): Número de éxitos.

        Devuelve:
            float: La probabilidad de obtener exactamente k éxitos.
        """
        return binom.pmf(k, self.n, self.p)

    def cdf(self, k):
        """
        Calcula la función de distribución acumulada hasta un número dado de éxitos.

        Parámetros:
            k (int): Número de éxitos.

        Devuelve:
            float: La probabilidad de obtener k o menos éxitos.
        """
        return binom.cdf(k, self.n, self.p)

class DistribucionPoisson:
    """
    Clase para calcular propiedades y probabilidades de la distribución de Poisson.
    """

    def __init__(self, mu):
        """
        Inicializa la distribución de Poisson con el parámetro de tasa (mu).

        Parámetros:
            mu (float): La tasa media de ocurrencia en un intervalo dado.
        """
        self.mu = mu

    def pmf(self, k):
        """
        Calcula la función de masa de probabilidad para un número dado de ocurrencias.

        Parámetros:
            k (int): Número de ocurrencias.

        Devuelve:
            float: La probabilidad de observar exactamente k ocurrencias.
        """
        return poisson.pmf(k, self.mu)

    def cdf(self, k):
        """
        Calcula la función de distribución acumulada para un número dado de ocurrencias.

        Parámetros:
            k (int): Número de ocurrencias.

        Devuelve:
            float: La probabilidad de observar k o menos ocurrencias.
        """
        return poisson.cdf(k, self.mu)

class DistribucionNormal:
    """
    Clase para calcular propiedades y probabilidades de la distribución normal.
    """

    def __init__(self, mu, sigma):
        """
        Inicializa la distribución normal con la media y la desviación estándar.

        Parámetros:
            mu (float): La media de la distribución.
            sigma (float): La desviación estándar de la distribución.
        """
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x):
        """
        Calcula la función de densidad de probabilidad en un punto dado.

        Parámetros:
            x (float): El punto en el que se evalúa la densidad de probabilidad.

        Devuelve:
            float: El valor de la densidad de probabilidad en x.
        """
        return norm.pdf(x, self.mu, self.sigma)

    def cdf(self, x):
        """
        Calcula la función de distribución acumulada hasta un punto dado.

        Parámetros:
            x (float): El punto hasta el cual se acumula la probabilidad.

        Devuelve:
            float: La probabilidad de que una observación sea menor o igual que x.
        """
        return norm.cdf(x, self.mu, self.sigma)

# Ejemplo de uso de las clases de distribución
if __name__ == "__main__":
    # Ejemplo de uso de la Distribución Binomial
    binomial = DistribucionBinomial(n=10, p=0.5)
    print("Distribución Binomial - PMF:", binomial.pmf(5))
    print("Distribución Binomial - CDF:", binomial.cdf(5))

    # Ejemplo de uso de la Distribución de Poisson
    poisson_dist = DistribucionPoisson(mu=3)
    print("Distribución de Poisson - PMF:", poisson_dist.pmf(5))
    print("Distribución de Poisson - CDF:", poisson_dist.cdf(5))

    # Ejemplo de uso de la Distribución Normal
    normal = DistribucionNormal(mu=0, sigma=1)
    print("Distribución Normal - PDF:", normal.pdf(0))
    print("Distribución Normal - CDF:", normal.cdf(0))

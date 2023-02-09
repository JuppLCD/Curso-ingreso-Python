'''
Curso de Nivelacion - Ingreso 2023
Calculo Algebraico - Seccion 2.2.
'''
from numpy.polynomial.polynomial import Polynomial
# import numpy as np
from functools import reduce


'''
La forma de colocar coeficientes es desde el polinomio de menor orden al mayor,
es decir, si tengo un polinomio [X^2 + 3X + 5] ==> la lista de coeficientes es [5, 3, 1]
'''

# Ver como expresar los polinomios en fomrato string
# polinomio = '-3x^2+1x+5'
# p = np.poly1d([1, 2, 3])
# print(np.poly1d(p)) => 1 x^2 + 2 x + 3
# print(np.poly1d([-3, 2, 7, 5])) => -3 x^3 + 2 x^2 + 7 x + 5


class Polinomio:
    def __init__(self) -> None:
        pass

    @ staticmethod
    def suma(*listas_coeficientes):
        polinomios = Polinomio._Polinomio__listas_coeficientes_a_polinomios(
            listas_coeficientes)
        resultado = reduce(lambda x, y: x+y, polinomios)

        Polinomio._Polinomio__print_resultado(resultado)

    @ staticmethod
    def resta(*listas_coeficientes):
        polinomios = Polinomio._Polinomio__listas_coeficientes_a_polinomios(
            listas_coeficientes)
        resultado = reduce(lambda x, y: x-y, polinomios)

        Polinomio._Polinomio__print_resultado(resultado)

    @ staticmethod
    def multiplicacion(*listas_coeficientes):
        polinomios = Polinomio._Polinomio__listas_coeficientes_a_polinomios(
            listas_coeficientes)
        resultado = reduce(lambda x, y: x*y, polinomios)

        Polinomio._Polinomio__print_resultado(resultado)

    @ staticmethod
    def divicion(polinomio_numerador, polinomio_denominador):
        nominador = Polynomial(coef=polinomio_numerador)
        denominador = Polynomial(coef=polinomio_denominador)

        cociente = nominador // denominador
        resto = nominador % denominador

        resultado = f'P(x) = Q(x) . D(x) + R(x) ===> P(x) = ( {cociente.convert()} ) . ( {denominador.convert()} ) + ( {resto.convert()} )'
        print(resultado)

    def __print_resultado(resultado):
        print(f'{resultado.convert()}')

    def __listas_coeficientes_a_polinomios(listas_coeficientes):
        return list(map(lambda coeficientes: Polynomial(coef=coeficientes), listas_coeficientes))

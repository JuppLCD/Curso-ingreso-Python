'''
Curso de Nivelacion - Ingreso 2023
Calculo Algebraico - Polinomios
'''
import sympy as sp
from functools import reduce


class Polinomio:
    def __init__(self) -> None:
        pass

    @ staticmethod
    def suma(*lista_polinomios_formato_texto):
        lista_polinomios = Polinomio._Polinomio__string_to_expression(
            lista_polinomios_formato_texto)
        resultado = reduce(lambda x, y: x+y, lista_polinomios)

        r, = Polinomio._Polinomio__poly_to_expression(resultado)
        print(r)

    @ staticmethod
    def resta(*lista_polinomios_formato_texto):
        lista_polinomios = Polinomio._Polinomio__string_to_expression(
            lista_polinomios_formato_texto)
        resultado = reduce(lambda x, y: x-y, lista_polinomios)

        r, = Polinomio._Polinomio__poly_to_expression(resultado)
        print(r)

    @ staticmethod
    def multiplicacion(*lista_polinomios_formato_texto):
        lista_polinomios = Polinomio._Polinomio__string_to_expression(
            lista_polinomios_formato_texto)
        resultado = reduce(lambda x, y: x*y, lista_polinomios)

        r, = Polinomio._Polinomio__poly_to_expression(resultado)
        print(r)

    @ staticmethod
    def divicion(polinomio_numerador, polinomio_denominador):
        numerador, denominador = Polinomio._Polinomio__string_to_expression(
            [polinomio_numerador, polinomio_denominador])

        cociente = numerador // denominador
        resto = numerador % denominador

        cociente, resto, denominador = Polinomio._Polinomio__poly_to_expression(
            cociente, resto, denominador)

        resultado = f'P(x) = Q(x) . D(x) + R(x) ===> P(x) = ( {cociente} ) . ( {denominador} ) + ( {resto} )'
        print(resultado)

    def __poly_to_expression(*poly_to_expression):
        return tuple(map(lambda p: p.as_expr(), poly_to_expression))

    def __string_to_expression(lista_polinomios):
        return tuple(map(lambda p: sp.Poly(sp.sympify(p)), lista_polinomios))

'''
Reolviendo ecuaciones lineales y sitema de ecuaciones lineales
'''

import numpy as np
from numpy.polynomial.polynomial import Polynomial
from fractions import Fraction


class EcuacionesLineales:
    def __init__(self) -> None:
        pass

    @ staticmethod
    def solucionar_ecuacion_lineal(coeficiente, solucion):
        resultado = np.linalg.solve(
            np.array([[coeficiente]]), np.array([solucion]))

        coef = coeficiente
        sol = solucion

        if (type(coeficiente) == float):
            coef = Fraction(str(coeficiente)).limit_denominator()

        if (type(solucion) == float):
            sol = Fraction(str(solucion)).limit_denominator()

        print(
            f'La solucion es ({resultado[0]}) a la escuacion lineal ({coef}x = {sol})')

    @ staticmethod
    def solucionar_sistema_ecuaciones_lineales(coeficientes: list, soluciones: list):
        '''
        coeficientes => [
                            [ coef_incognita_1, coef_incognita_2, ( ... ), coef_incognita_n ] ==> ecuacion_1 ,
                            [ coef_incognita_1, coef_incognita_2, ( ... ), coef_incognita_n ] ==> ecuacion_2 ,
                                                    ( ... )                                    ( ... )   ,
                            [ coef_incognita_1, coef_incognita_2, ( ... ), coef_incognita_n ]  ==> ecuacion_n
                        ]
        soluciones => [ [ solucion_ecuacion_1, solucion_ecuacion_2, ( ... ), solucion_ecuacion_3 ] ]
        '''
        resultados = np.linalg.solve(
            np.array(coeficientes), np.array(soluciones))

        mensaje = 'Los resultados son: '
        for i, resultado in enumerate(resultados):
            mensaje += f'( {i+1}_incognita = {resultado} ), '

        mensaje.strip()
        print(mensaje[:-2])


class EcuacionesCuadraticas:
    def __init__(self) -> None:
        pass

    @ staticmethod
    def calcular_discriminante(coeficientes: list):
        '''
        coeficientes = [ c, b, a]
        c = termino independiente
        b = termino con incognita grado 1
        a = termino con incognita grado 2
        '''

        discriminante = EcuacionesCuadraticas._EcuacionesCuadraticas__discriminante(
            coeficientes)

        msg = f'El discriminante es {discriminante}, por lo tanto posee '
        if (discriminante < 0):
            msg += '2 raices complejas'
        elif (discriminante > 0):
            msg += '2 raices reales y distintas'
        else:
            msg += 'una unica raiz doble'

        print(msg)
        return discriminante

    @ staticmethod
    def obtener_raices(coeficientes: list):
        '''
        coeficientes = [ c, b, a]
        c = termino independiente
        b = termino con incognita grado 1
        a = termino con incognita grado 2
        '''
        polinomio_2_grado = Polynomial(coef=coeficientes)
        raices = polinomio_2_grado.roots()

        EcuacionesCuadraticas._EcuacionesCuadraticas__mostrar_raices(
            coeficientes, raices)

    def __discriminante(coeficientes):
        a = coeficientes[2]
        b = coeficientes[1]
        c = coeficientes[0]

        resultado = (b**2) - 4 * a * c
        return resultado

    def __mostrar_raices(coeficientes, raices):
        discriminante = EcuacionesCuadraticas._EcuacionesCuadraticas__discriminante(
            coeficientes)

        if (discriminante != 0):
            msg = 'Las raices son: '

            for i, raiz in enumerate(raices):
                msg += f'x{i+1} = {raiz}, '

            msg = msg.strip()[:-2]

            print(msg)
            print(
                f'La ecuacion simplificada es {coeficientes[2]}( x - ({raices[0]}) )( x - ({raices[1]}) )')

        else:
            print(f'La raiz es {raices[0]}')
            print(
                f'La ecuacion simplificada es {coeficientes[2]}.( x{raices[0]} )^2')

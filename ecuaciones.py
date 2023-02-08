'''
Reolviendo ecuaciones lineales y sitema de ecuaciones lineales
'''

import numpy as np
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


# 3/7 x = 4 + 2/7
# EcuacionesLineales.solucionar_ecuacion_lineal(3/7, 4 + (2/7))

# x + y = 5
# 2x − y = 7
# EcuacionesLineales.solucionar_sistema_ecuaciones_lineales(
#     [[1, 1], [2, -1]], [5, 7])

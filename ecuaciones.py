'''
Reolviendo ecuaciones lineales y sitema de ecuaciones lineales
'''

import sympy as sp


class EcuacionesLineales:
    symbols = sp.symbols('x,y')

    def __init__(self) -> None:
        pass

    @ staticmethod
    def solucionar_ecuacion_lineal(ecuacion_texto: str, solucion: float | int):
        ecuacion = sp.Eq(sp.sympify(ecuacion_texto), solucion)

        resultado = sp.solve(ecuacion, EcuacionesLineales.symbols[0])

        print(
            f'La solucion es ({resultado[0]}) a la escuacion lineal ({ecuacion_texto} = {solucion})')

    @ staticmethod
    def solucionar_sistema_ecuaciones_lineales(ecuaciones: tuple):
        '''
        ecuaciones => [
                            ecuacion_1 ,
                            ecuacion_2 ,
                            ( ... ),
                            ecuacion_n
                        ]

        Ejemplo:
            "x + y = 5",
            "2x - y = 7";

            ecuaciones = ("x + y - 5", "2*x - y - 7")
        '''
        sistema_ecuaciones = []

        for ecuacion in ecuaciones:
            sistema_ecuaciones.append(sp.sympify(ecuacion))

        r = sp.solve(sistema_ecuaciones, *EcuacionesLineales.symbols)

        if (len(r) == 0):
            print('Determinante es 0, ver si tiene infinitas soluciones o no')

        print('Los resultados son: ', r)


class EcuacionesCuadraticas:
    symbols = sp.symbols('x,y')

    def __init__(self) -> None:
        pass

    @ staticmethod
    def calcular_discriminante(ecuacion: str):
        '''
        Ejemplo:
            "x^2 - 5x + 6",
            ecuacion = "x**2 - 5*x + 6"
        '''
        ecuacion_2_grado = sp.sympify(ecuacion)
        coeficientes = sp.Poly(ecuacion_2_grado).all_coeffs()

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
    def obtener_raices(ecuacion: str):
        '''
        Ejemplo:
            "x^2 - 5x + 6",
            ecuacion = "x**2 - 5*x + 6"
        '''

        ecuacion_2_grado = sp.sympify(ecuacion)
        raices = sp.solve(ecuacion_2_grado, EcuacionesCuadraticas.symbols[0])

        coeficientes = sp.Poly(ecuacion_2_grado).all_coeffs()

        EcuacionesCuadraticas._EcuacionesCuadraticas__mostrar_raices(
            coeficientes, raices)

    def __discriminante(coeficientes):
        a = coeficientes[0]
        b = coeficientes[1]
        c = coeficientes[2]

        resultado = (b**2) - 4 * a * c
        return resultado

    def __mostrar_raices(coeficientes, raices):
        discriminante = EcuacionesCuadraticas._EcuacionesCuadraticas__discriminante(
            coeficientes)

        if (discriminante != 0):
            msg = 'Las raices son: '

            for i, raiz in enumerate(raices):
                msg += f'x{i+1} = {raiz}, '

            msg = msg.strip()[:-1]

            print(msg)
            print(
                f'La ecuacion simplificada es {coeficientes[0]}( x - ({raices[0]}) )( x - ({raices[1]}) )')

        else:
            print(f'La raiz es {raices[0]}')
            print(
                f'La ecuacion simplificada es {coeficientes[0]}( x - ({raices[0]}) )^2')

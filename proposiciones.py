'''
Curso de Nivelacion - Ingreso 2023
Logica - Tablas de verdad
'''


class TablasDeVerdad:
    valores = (True, False)

    def __init__(self) -> None:
        pass

    @ staticmethod
    def conjuncion():
        TablasDeVerdad.pintar_tabla(
            TablasDeVerdad, 'p \t | q \t \t | p ∧ q ', 'and')

    @ staticmethod
    def disyuncion():
        TablasDeVerdad.pintar_tabla(
            TablasDeVerdad, 'p \t | q \t \t | p v q ', 'or')

    @ staticmethod
    def disyuncion_exclusiva():
        TablasDeVerdad.pintar_tabla(
            TablasDeVerdad, 'p \t | q \t \t | p ⊻ q ', 'xor')

    @ staticmethod
    def implicacion():
        TablasDeVerdad.pintar_tabla(
            TablasDeVerdad, 'p \t | q \t \t | p ⇒ q ', '==>')

    @ staticmethod
    def implicacion_doble():
        TablasDeVerdad.pintar_tabla(
            TablasDeVerdad, 'p \t | q \t \t | p ⇔ q ', '<==>')

    @ staticmethod
    def negacion():
        TablasDeVerdad.pintar_tabla(
            TablasDeVerdad, 'p \t | ¬ p ', 'not', '{p} \t | {valor_verdad}')

    def pintar_tabla(self, titulo, operador_logico, tabla='{p} \t | {q} \t | {valor_verdad}'):
        print(titulo)
        for p in self.valores:
            for q in self.valores:
                valor_verdad = self.valor_de_verdad(p, q, operador_logico)
                print(tabla.format(p=p, q=q, valor_verdad=valor_verdad))

    def valor_de_verdad(p, q, operador_logico):
        if (operador_logico == 'and'):
            return p and q
        if (operador_logico == 'or'):
            return p or q
        if (operador_logico == 'xor'):
            return (p or q) and not (p and q)
        if (operador_logico == '==>'):
            return not (p) or q
        if (operador_logico == '<==>'):
            return (not (p) or q) and (not (q) or p)
        if (operador_logico == 'not'):
            # p == q
            return not p

        return 'Error'

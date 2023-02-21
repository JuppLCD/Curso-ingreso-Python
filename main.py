# from ecuaciones import EcuacionesLineales, EcuacionesCuadraticas
# from proposiciones import TablasDeVerdad

# ECUACIONES

# ECUACIONES LINEALES
# 30x = 5
# EcuacionesLineales.resolver('x*30', 5)

# Sistema de ecuacion lineal
# Unica solucion
# 'x + y = 5' , '2x − y = 7'
# EcuacionesLineales.resolver_sistema_ecuaciones_lineales(
#     ('x + y - 5', '2*x - y - 7'))

# Sin Solucion
# EcuacionesLineales.resolver_sistema_ecuaciones_lineales(
#     ('2*x - y - 5', '2*x - y - 7'))

# Infinitas soluciones
# EcuacionesLineales.resolver_sistema_ecuaciones_lineales()


# ECUACIONES CUADRATICAS
# Ecuacion con 2 raices reales
# x^2 − 5x + 6 = 0
# EcuacionesCuadraticas.calcular_discriminante("x**2 - 5*x + 6")
# EcuacionesCuadraticas.resolver("x**2 - 5*x + 6")

# Ecuacion con 2 raices complejas
# x^2 + 4
# EcuacionesCuadraticas.calcular_discriminante("x**2 + 4")
# EcuacionesCuadraticas.resolver("x**2 + 4")

# Ecuacion con raiz unica y doble
# x^2 + 4x + 4
# EcuacionesCuadraticas.calcular_discriminante('x**2 + 4*x + 4')
# EcuacionesCuadraticas.resolver('x**2 + 4*x + 4')

# PROPOSICIONES

# Creando las tablas de verdad para los simbolos logicos mas comunes
# TablasDeVerdad.conjuncion()
# TablasDeVerdad.disyuncion()
# TablasDeVerdad.disyuncion_exclusiva()
# TablasDeVerdad.implicacion()
# TablasDeVerdad.implicacion_doble()
# TablasDeVerdad.negacion()

# FUNCIONES

# Obtener Vertices
# x^2 => v = (0,0)
# EcuacionesCuadraticas.vertice('x**2')
# x^2 + 2x - 3 => v = (-1,-4)
# EcuacionesCuadraticas.vertice('x**2 + 2*x -3')

# Grafica de funciones lineales y cuadraticas
# EcuacionesLineales.graficar('2*x +5')
# EcuacionesCuadraticas.graficar('x**2 + 2*x -3')

import Quantum as q
import ComplexLibrary as cl

sx = [[0, 1],
      [1, 0]]
sy = [[0, -1j],
      [1j, 0]]
sz = [[1, 0],
      [0, -1]]

def mostrarRespuesta4_3_1(observable):
    x, v = q.EigenValues(observable)
    answ = []
    for el in v:
        current = q.translateEightnVector(el)
        answ.append(current)
    return answ

def mostrarRespuesta4_3_2(observable):
    shi = [[1, 0], [0, 0]]
    x, v = q.EigenValues(observable)

    meanValueDistribution = [0, 0]
    for i in range(len(x)):
        eigenValue = q.translateValues(x[i])
        eigenVector = q.translateEightnVector(v[:, i])

        prob = cl.complexProduct(eigenValue, [q.longitud([q.transicion(eigenVector, shi)]) ** 2, 0])

        meanValueDistribution = cl.complexSum(meanValueDistribution, prob)
    return meanValueDistribution

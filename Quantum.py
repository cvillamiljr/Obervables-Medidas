from sys import stdin
import ComplexLibrary as cl
import math
import numpy as np

def dosdecimales(num, undecimal):
    num = "{:.2f}".format(num)
    num = (num[:-1] if undecimal else num)
    return float(num)


def longitud(vect):

    acu = 0
    for x in range(len(vect)):
        acu += (cl.complexMod(vect[x])) ** 2
    return math.sqrt(acu)


def normalizar(vect):
    length = len(vect)
    for x in range(len(vect)):
        vect[x] = [vect[x][0] / length, vect[x][1] / length]
    return vect


def bra(vect):

    return cl.dagaMatriz(vect)


def transicion(vect1, vect2):
    
    return cl.multiVectores(vect1, vect2)

def probability(vector, position):
    lon = longitud(vector)
    if (0 <= position < len(vector)):
        return dosdecimales(cl.complexMod(vector[position]) ** 2 / lon ** 2, False)


def omegaPsi(psi, omega):
    return cl.innerProduct(cl.accionmatrizvector(omega, psi), psi)[0]


def deltaPsi(omega, expectedValue):
    return cl.complexRest(omega, cl.escalarXMatriz(expectedValue, cl.identityMatrix(omega)))


def matrixPsi(matrix, psi):
    cl.accionmatrizvector(matrix, cl.dagaMatriz(psi))
    vect = cl.accionmatrizvector(matrix, cl.dagaMatriz(psi))
    return dosdecimales(cl.matrixProduct(vect, cl.dagaMatriz(psi))[0], False)


def variance(psi, omega):
    expectedValue = dosdecimales(omegaPsi(psi, omega), True)
    delta = deltaPsi(omega, [expectedValue, 0.0])
    matrixOfVariance = cl.matrixProduct(delta, delta)
    return matrixPsi(matrixOfVariance, psi)


def describeAnObservable(psi, matrix):
    if (cl.esHermitiana(matrix)):
        mean = dosdecimales(omegaPsi(psi, matrix), True)
        return [variance(psi, matrix), mean]
    return None


def translateEightnVector(vector):
    answ = []
    for el in vector:
        answ.append([el.real, el.imag])
    return answ


def translateValues(val):
    return [val.real, val.imag]


def EigenValues(omega):
    observable = np.array(omega)
    x, v = np.linalg.eig(observable)
    return x, v

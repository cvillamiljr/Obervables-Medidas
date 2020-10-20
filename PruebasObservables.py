import Ejercicios as e
import ComplexLibrary as cl
import unittest
import math
import clasicToQuantum as c

sx = [[0, 1],
      [1, 0]]
sy = [[0, -1j],
      [1j, 0]]
sz = [[1, 0],
      [0, -1]]


class observableTest(unittest.TestCase):

    def testExercice4_3_1(self):
        self.assertEqual(e.mostrarRespuesta4_3_1(sx), [[[0.7071067811865475, 0.0], [-0.7071067811865475, 0.0]],
                                                     [[0.7071067811865475, 0.0], [0.7071067811865475, 0.0]]])
        self.assertEqual(e.mostrarRespuesta4_3_1(sy), [[[-0.0, -0.7071067811865474], [0.7071067811865475, 0.0]],
                                                     [[0.7071067811865476, 0.0], [0.0, -0.7071067811865475]]])
        self.assertEqual(e.mostrarRespuesta4_3_1(sz), [[[1.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [1.0, 0.0]]])

    def testExercice4_3_2(self):
        self.assertEqual(e.mostrarRespuesta4_3_2(sx), (0.0, 0.0))
        self.assertEqual(e.mostrarRespuesta4_3_2(sy), (-2.7755575615628914e-16, 0.0))
        self.assertEqual(e.mostrarRespuesta4_3_2(sz), (1.0, 0.0))

    def testExercice4_4_1(self):
        raiz = math.sqrt(2) / 2
        u1 = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
        u2 = [[[raiz, 0], [raiz, 0]], [[raiz, 0], [-raiz, 0]]]
        self.assertEqual(cl.esUnitaria(u1), True)
        self.assertEqual(cl.esUnitaria(u2), True)
        self.assertEqual(cl.esUnitaria(cl.matrixProduct(u1, u2)), True)
        self.assertEqual(cl.esUnitaria(cl.matrixProduct(u1, u2)), True)

    def testExercice4_4_2(self):
        raiz = 1 / math.sqrt(2)
        vectIni = [[1, 0], [0, 0], [0, 0], [0, 0]]
        matrix = [[[0, 0], [raiz, 0], [raiz, 0], [0, 0]],
                  [[0, raiz], [0, 0], [0, 0], [raiz, 0]],
                  [[raiz, 0], [0, 0], [0, 0], [0, raiz]],
                  [[0, 0], [raiz, 0], [-raiz, 0], [0, 0]]]
        self.assertEqual(c.sistemaprobabilisticoquantico(matrix, vectIni, 3),
                         [[[0.4999999999999996, 0], [0.0, 0], [0.0, 0], [0.4999999999999996, 0]],
                          [[0.0, 0], [0.4999999999999996, 0], [0.4999999999999996, 0], [0.0, 0]],
                          [[0.0, 0], [0.4999999999999996, 0], [0.4999999999999996, 0], [0.0, 0]],
                          [[0.4999999999999996, 0], [0.0, 0], [0.0, 0], [0.4999999999999996, 0]]])


if __name__ == '__main__':
    unittest.main()
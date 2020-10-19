import unittest
import math 
import ComplexLibrary
class pruebaComplejos(unittest.TestCase):

    def test_sum(self):
        ans1 = ComplexLibrary.complexSum((10,10),(20,20))
        ans2 = ComplexLibrary.complexSum((-2,-3),(-5,-3))
        ans3 = ComplexLibrary.complexSum((-1,9),(1,3))
        self.assertEqual(ans1,(30, 30))
        self.assertEqual(ans2,(-7, -6))
        self.assertEqual(ans3,(0, 12))
        
    def test_resta(self):
        ans1 = ComplexLibrary.complexRest((10,10),(20,20))
        ans2 = ComplexLibrary.complexRest((-2,-3),(-5,-3))
        ans3 = ComplexLibrary.complexRest((-1,9),(1,3))
        self.assertEqual(ans1,(-10, -10))
        self.assertEqual(ans2,(3, 0))
        self.assertEqual(ans3,(-2, 6))

    def test_Product(self):
        ans = ComplexLibrary.complexProduct((4,6),(1,4))
        self.assertEqual(ans,(-20,22))

    def test_div(self):
        ans = ComplexLibrary.complexDiv((100,20),(2,4))
        self.assertEqual(ans,(14.0, -18.0))

    def test_mod(self):
        self.assertEqual(ComplexLibrary.complexMod((5,5)),25)
        self.assertEqual(ComplexLibrary.complexMod((3,9)),45)
        self.assertEqual(ComplexLibrary.complexMod((-3,-6)),22.5)

    def test_conjugado(self):
        self.assertEqual(ComplexLibrary.complexConj((3,21)),(3,-21))
        self.assertEqual(ComplexLibrary.complexConj((6,-76)),(6,76))
        self.assertEqual(ComplexLibrary.complexConj((5,16)),(5,-16))

    def test_polarCartesiano(self):
        self.assertEqual(ComplexLibrary.polarCartesiano((13,23)),(11.966563094881725,5.079504670360558))
        self.assertEqual(ComplexLibrary.polarCartesiano((2,120)),(-0.9999999999999996,1.7320508075688774))
        self.assertEqual(ComplexLibrary.polarCartesiano((1,0)),(1,0))
        
    def test_cartesianoPolar(self):
        self.assertEqual(ComplexLibrary.cartesianoPolar((1,2)),(2.23606797749979,63.43494882292201))
        self.assertEqual(ComplexLibrary.cartesianoPolar((-3,1)),(3.1622776601683795,18.43494882292201))
        self.assertEqual(ComplexLibrary.cartesianoPolar((2,2)),(2.8284271247461903,45.0))

    def test_argu(self):
        self.assertEqual(ComplexLibrary.complexArg((3,21)),1.4288992721907328)
        self.assertEqual(ComplexLibrary.complexArg((6,-76)),-1.492012365805753)
        self.assertEqual(ComplexLibrary.complexArg((5,16)),1.2679114584199251)

    
    def test_sumaVectores(self):
        ans1 = ComplexLibrary.adicionVectores([(1,2),(1,2),(3,5)],[(-2,2),(2,2),(4,10)])
        ans2 = ComplexLibrary.adicionVectores([(1,0),(1,-2),(3,2)],[(2,2),(3,2),(4,5)])
        self.assertEqual(ans1,[(-1,4),(3,4),(7,15)])
        self.assertEqual(ans2,[(3,2),(4,0),(7,7)])
        
    def test_inversaVector(self):
        ans1 = ComplexLibrary.inversaVector([(1,-1),(2,3),(-1,3)])
        ans2 = ComplexLibrary.inversaVector([(1,2),(-3,3),(-1,3)])
        self.assertEqual(ans1,[(-1,1),(-2,-3),(1,-3)])
        self.assertEqual(ans2,[(-1,-2),(3,-3),(1,-3)])
        

    def test_sumaMatrices(self):
        ans1 = ComplexLibrary.sumaMatrices([[(1,1),(2,-3)],[(4,2),(2,4)]],[[(1,0),(1,0)],[(1,0),(1,0)]])
        ans2 = ComplexLibrary.sumaMatrices([[(1,3),(2,3)],[(1,3),(2,3)]],[[(1,0),(3,6)],[(1,0),(3,6)]])
        self.assertEqual(ans1,[[(2,1),(3,-3)],[(5,2),(3,4)]])
        self.assertEqual(ans2,[[(2,3),(5,9)],[(2,3),(5,9)]])

    def test_inversaMatriz(self):
        ans1 = ComplexLibrary.inversaMatriz([[(1,1),(2,-3)],[(4,2),(2,4)]])
        ans2 = ComplexLibrary.inversaMatriz([[(1,1),(0,3)],[(-1,2),(-2,4)]])
        self.assertEqual(ans1,[[(-1,-1),(-2,3)],[(-4,-2),(-2,-4)]])
        self.assertEqual(ans2,[[(-1,-1),(0,-3)],[(1,-2),(2,-4)]])

    def multiplicacionEscalarMatrices(self):
        ans1 = ComplexLibrary.escalarXMatriz([[(1,1),(2,-3)],[(4,2),(2,4)]],(1,1))
        ans2 = ComplexLibrary.escalarXMatriz([[(1,1),(2,-3)],[(4,2),(2,4)]],(2,3))
        self.assertEqual(ans1,[[(0,2),(5,-1)],[(2,6),(-2,6)]])
        self.assertEqual(ans2,[[(-1,5),(13,0)],[(2,16),(-8,14)]])

    def test_transpuesta(self):
        ans1 = ComplexLibrary.transpuestaMatriz([[(1,1),(2,-3)],[(4,2),(2,4)]])
        ans2 = ComplexLibrary.transpuestaMatriz([[(1,1),(2,-3),(5,4)],[(4,2),(2,4),(4,5)]])
        self.assertEqual(ans1,[[(1,1),(4,2)],[(2,-3),(2,4)]])
        self.assertEqual(ans2,[[(1,1),(4,2)],[(2,-3),(2,4)],[(5,4),(4,5)]])
        
    def test_conjugadoMatriz(self):
        ans1 = ComplexLibrary.conjugadoMatriz([[(1,2),(2,1)],[(1,-2),(2,-3)],[(3,4),(3,-1)]])
        ans2 = ComplexLibrary.conjugadoMatriz([[(1,1),(2,2),(1,1)],[(2,2),(3,-3),(2,3)]])
        self.assertEqual(ans1,[[(1,-2),(2,-1)],[(1,2),(2,3)],[(3,-4),(3,1)]])
        self.assertEqual(ans2,[[(1,-1),(2,-2),(1,-1)],[(2,-2),(3,3),(2,-3)]])

    def test_matrizAdjunta(self):
        ans1 = ComplexLibrary.dagaMatriz([[(1,1),(2,-3)],[(4,2),(2,4)]])
        ans2 = ComplexLibrary.dagaMatriz([[(1,1),(2,3)],[(4,2),(1,4)],[(1,0),(3,-4)]])
        self.assertEqual(ans1,[[(1,-1),(4,-2)],[(2,3),(2,-4)]])
        self.assertEqual(ans2,[[(1,-1),(4,-2),(1,0)],[(2,-3),(1,-4),(3,4)]])


    def test_productoInternoVectores(self):
        ans1 = ComplexLibrary.innerProduct([(1,0),(0,1),(1,-3)],[(2,1),(0,1),(2,0)])
        ans2 = ComplexLibrary.innerProduct([(1,-2),(-2,1),(4,3)],[(2,1),(1,-3),(3,0)])
        self.assertEqual(ans1,(5,7))
        self.assertEqual(ans2,(7,1))

    def test_normaMatriz(self):
        self.assertEqual(ComplexLibrary.normaVector([(3,0),(-6,0),(-2,0)]),7.0)
        self.assertEqual(ComplexLibrary.normaVector([(2,0),(4,0)]),4.47213595499958)
        self.assertEqual(ComplexLibrary.normaVector([(4,0),(3,0)]),5.0)

    def test_distanciaVectores(self):
        ans1 = ComplexLibrary.distanciaVectores([(0,0),(0,0)],[(1,1),(2,4)])
        ans2 = ComplexLibrary.distanciaVectores([(1,2),(2,5)],[(2,6),(5,3)])
        self.assertEqual(ans1,4.69041575982343)
        self.assertEqual(ans2,5.477225575051661)
        


    def test_esUnitaria(self):
        self.assertFalse(ComplexLibrary.esUnitaria([[(1,1),(0,0)],[(0,0),(1,-1)]]))
        self.assertFalse(ComplexLibrary.esUnitaria([[(-1,0),(0,-1)],[(0,1),(1,0)]]))
        self.assertTrue(ComplexLibrary.esUnitaria([[(0,0),(1,0)],[(1,0),(0,0)]]))
        
    def test_esHermitiana(self):
        self.assertFalse(ComplexLibrary.esHermitiana([[(1,1),(0,0)],[(0,0),(1,-1)]]))
        self.assertTrue(ComplexLibrary.esHermitiana([[(-1,0),(0,-1)],[(0,1),(1,0)]]))
        self.assertTrue(ComplexLibrary.esUnitaria([[(0,0),(1,0)],[(1,0),(0,0)]]))

    def test_productoTensorVectores(self):
        ans1 = ComplexLibrary.productoTensorVectores([(-1,0),(2,0),(5,0)],[(4,0),(-3,0)])
        ans2 = ComplexLibrary.productoTensorVectores([(-1,1),(2,-1),(5,1)],[(4,1),(3,0)])
        self.assertEqual(ans1,[(-4,0),(3,0),(8,0),(-6,0),(20,0),(-15,0)])
        self.assertEqual(ans2,[(-5,3),(-3,3),(9,-2),(6,-3),(19,9),(15,3)])
        

if __name__ == "__main__":
    unittest.main()

import unittest
from pycalc import pycalc
import math


class TestWrongInput(unittest.TestCase):
    def test_comparison(self):
        self.assertTrue(pycalc.functions_evaluation('8*3==6*4'))
        self.assertTrue(pycalc.functions_evaluation('4/3+1!=4/3+2'))
        self.assertTrue(pycalc.functions_evaluation('6*(1+3)<7*(1+3)'))
        self.assertTrue(pycalc.functions_evaluation('-4/-1>4/-1'))
        self.assertTrue(pycalc.functions_evaluation('7^3<=7^3'))
        self.assertTrue(pycalc.functions_evaluation('7^2<=7^3'))
        self.assertTrue(pycalc.functions_evaluation('7%2>=10%3'))
        self.assertTrue(pycalc.functions_evaluation('11*8-5>=11*(8-5)'))
        self.assertFalse(pycalc.functions_evaluation('8*3!=6*4'))
        self.assertFalse(pycalc.functions_evaluation('4/3+1==4/3+2'))
        self.assertFalse(pycalc.functions_evaluation('6*(1+3)>7*(1+3)'))
        self.assertFalse(pycalc.functions_evaluation('-4/-1<4/-1'))
        self.assertFalse(pycalc.functions_evaluation('7^2>=7^3'))
        self.assertFalse(pycalc.functions_evaluation('11*8-5<=11*(8-5)'))

    def test_unar(self):
        self.assertEqual(pycalc.functions_evaluation("+.5"), .5)
        self.assertEqual(pycalc.functions_evaluation("-.5"), -.5)
        self.assertEqual(pycalc.functions_evaluation("+-.5"), +-.5)
        self.assertEqual(pycalc.functions_evaluation("-abs(5)"), -abs(5))
        self.assertEqual(pycalc.functions_evaluation("500"), +-+-500)
        self.assertEqual(pycalc.functions_evaluation("--------------+5"), --------------+5)

    def test_math_module(self):
        self.assertEqual(pycalc.functions_evaluation("abs(-254.5)"), abs(-254.5))
        self.assertEqual(pycalc.functions_evaluation("round(-254.4)"), round(-254.4))
        self.assertEqual(pycalc.functions_evaluation("ceil(-254.3)"), math.ceil(-254.3))
        self.assertEqual(pycalc.functions_evaluation("copysign(-254.5,11)"), math.copysign(-254.5, 11))
        self.assertEqual(pycalc.functions_evaluation("fabs(-254.5)"), math.fabs(-254.5))
        self.assertEqual(pycalc.functions_evaluation("factorial(10)"), math.factorial(10))
        self.assertEqual(pycalc.functions_evaluation("floor(-11.2)"), math.floor(-11.2))
        self.assertEqual(pycalc.functions_evaluation("fmod(12,11)"), math.fmod(12, 11))
        self.assertEqual(pycalc.functions_evaluation("isfinite(12)"), math.isfinite(12))
        self.assertEqual(pycalc.functions_evaluation("isinf(3)"), math.isinf(3))
        self.assertEqual(pycalc.functions_evaluation("isnan(110)"), math.isnan(110))
        self.assertEqual(pycalc.functions_evaluation("trunc(12.11)"), math.trunc(12.11))


if __name__ == '__main__':
    unittest.main()

import unittest
from pycalc import pycalc


class TestWrongInput(unittest.TestCase):
    def test_comparison(self):
        # self.assertTrue(calc('8*3==6*4'))
        self.assertTrue(pycalc.functions_evaluation('4/3+1!=4/3+2'))
        # self.assertTrue(target.functions_evaluation('6*(1+3)<7*(1+3)'))
        # self.assertTrue(target.functions_evaluation('-4/-1>4/-1'))
        # self.assertTrue(target.functions_evaluation('7^3<=7^3'))
        # self.assertTrue(target.functions_evaluation('7^2<=7^3'))
        # self.assertTrue(target.functions_evaluation('7%2>=10%3'))
        # self.assertTrue(target.functions_evaluation('11*8-5>=11*(8-5)'))
        # self.assertFalse(target.functions_evaluation('8*3!=6*4'))
        # self.assertFalse(target.functions_evaluation('4/3+1==4/3+2'))
        # self.assertFalse(target.functions_evaluation('6*(1+3)>7*(1+3)'))
        # self.assertFalse(target.functions_evaluation('-4/-1<4/-1'))
        # self.assertFalse(target.functions_evaluation('7^2>=7^3'))
        # self.assertFalse(target.functions_evaluation('11*8-5<=11*(8-5)'))


if __name__ == '__main__':
    unittest.main()

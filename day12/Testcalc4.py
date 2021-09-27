from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from calc import Calc
da=[
    [100,5,20],
    [110,2,55],
    [-9,-3,3],
    [6,3,2],
    [2,2,1],
    [3,-3,1]
]
@ddt
class Testcalc(TestCase):
    @data(*da)
    @unpack
    def testsubs(self,a,b,c):
        calc=Calc()
        sum=calc.devision(a,b)
        self.assertEqual(sum,c)




























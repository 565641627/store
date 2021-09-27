from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from calc import Calc
da=[
    [105,47,58],
    [110,55,55],
    [10,5,5],
    [6,3,3],
    [0,-2,2],
    [3,-3,6]
]
@ddt
class Testcalc(TestCase):
    @data(*da)
    @unpack
    def testsubs(self,a,b,c):
        calc=Calc()
        sum=calc.subs(a,b)
        self.assertEqual(sum,c)




























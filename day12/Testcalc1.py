from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from calc import Calc
da=[
    [47,58,105],
    [55,55,110],
    [5,5,10],
    [3,3,5],
    [0,-2,-2],
    [1000000000000000000000000000000000000000000000000000000000000000000000000000000,
     3,
     1000000000000000000000000000000000000000000000000000000000000000000000000000003]
]
@ddt
class Testcalc(TestCase):
    @data(*da)
    @unpack
    def testadd(self,a,b,c):
        calc=Calc()
        sum=calc.add(a,b)
        self.assertEqual(sum,c)




























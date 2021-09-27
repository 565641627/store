from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from calc import Calc
da=[
    [5,25,125],
    [180,125,22500],
    [68,-13,-884],
    [-16,-99,1584],
    [43534534,0,3],
    [32432.6,322.5,10459513.5]
]
@ddt
class Testcalc(TestCase):
    @data(*da)
    @unpack
    def testsubs(self,a,b,c):
        calc=Calc()
        sum=calc.multi(a,b)
        self.assertEqual(sum,c)




























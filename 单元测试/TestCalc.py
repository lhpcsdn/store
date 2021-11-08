from Calc import Calc
from unittest import TestCase


class TestCalc(TestCase):

    def testAdd1(self):
        a = 1
        b = 2
        c = 3

        calc = Calc()
        sum = calc.add(a, b)
        self.assertEqual(c, sum)

    def testAdd2(self):
        a = -1
        b = 1
        c = 0

        calc = Calc()
        sum = calc.add(a, b)
        self.assertEqual(c, sum)

    def testAdd3(self):
        a = -1
        b = -1
        c = -2

        calc = Calc()
        sum = calc.add(a, b)
        self.assertEqual(c, sum)

    def testAdd4(self):
        a = 1
        b = -1
        c = 0

        calc = Calc()
        sum = calc.add(a, b)
        self.assertEqual(c, sum)

    def testminus1(self):
        a = 1
        b = 1
        c = 0

        calc = Calc()
        d = calc.minus(a, b)
        self.assertEqual(c, d)

    def testminus2(self):
        a = -1
        b = -1
        c = 0

        calc = Calc()
        d = calc.minus(a, b)
        self.assertEqual(c, d)

    def testminus3(self):
        a = 1
        b = -1
        c = 2

        calc = Calc()
        d = calc.minus(a, b)
        self.assertEqual(c, d)

    def testminus4(self):
        a = -1
        b = 1
        c = -2

        calc = Calc()
        d = calc.minus(a, b)
        self.assertEqual(c, d)

    def testmulti1(self):
        a = 2
        b = 2
        c = 4

        calc = Calc()
        d = calc.multi(a, b)
        self.assertEqual(c, d)

    def testmulti2(self):
        a = -2
        b = -1
        c = 2

        calc = Calc()
        d = calc.multi(a, b)
        self.assertEqual(c, d)

    def testmulti3(self):
        a = 2
        b = -1
        c = -2

        calc = Calc()
        d = calc.multi(a, b)
        self.assertEqual(c, d)

    def testmulti4(self):
        a = -1
        b = 2
        c = -2

        calc = Calc()
        d = calc.multi(a, b)
        self.assertEqual(c, d)

    def testdevision1(self):
        a = 2
        b = 2
        c = 1

        calc = Calc()
        d = calc.devision(a, b)
        self.assertEqual(c, d)

    def testdevision2(self):
        a = -2
        b = -1
        c = 2

        calc = Calc()
        d = calc.devision(a, b)
        self.assertEqual(c, d)

    def testdevision3(self):
        a = 2
        b = -1
        c = -2

        calc = Calc()
        d = calc.devision(a, b)
        self.assertEqual(c, d)

    def testdevision4(self):
        a = -4
        b = 2
        c = -2

        calc = Calc()
        d = calc.devision(a, b)
        self.assertEqual(c, d)

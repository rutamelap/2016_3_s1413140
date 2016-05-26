import unittest
import surinktuvas
import traukinys
#  https://docs.python.org/3.5/library/unittest.html
#  https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/

class TestPridetasLokomotyvas(unittest.TestCase):
    def test_pridetasLokomotyvas(self):
        self.assertIsNone(traukinys.Traukinys.pridetasLokomotyvas(
            traukinys.Traukinys(1112,[100, 100, 1111]),[100, 100, 1111]))

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertIsNone(traukinys.Traukinys.__add__(
            traukinys.Traukinys(1112,[100, 100, 100, 1111]),[100, 100, 100, 1111]))

class TestUzimtasNeleidziamasVagonai(unittest.TestCase):
    def test_uzimtasNeleidziamasVagonai(self):
        self.assertFalse(traukinys.Traukinys.uzimtasNeleidziamasVagonai(
            traukinys.Traukinys(1112, False), 1112))

class TestSub(unittest.TestCase):
	def test_sub(self):
		self.assertIsNone(traukinys.Traukinys.__sub__(
			traukinys.Traukinys(1112,[100, 100, 100, 1111]),[100, 100, 100, 1111]))

class TestKurtiLokomotyva(unittest.TestCase):
	def test_kurtiLokomotyva(self):
		self.assertIsNone(surinktuvas.kurtiLokomotyva(
			surinktuvas.surinktuvas(100,100,1112,[100,100,1112]),[100,100,1112]))

if __name__ == '__main__':
    unittest.main()

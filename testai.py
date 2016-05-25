import unittest
import surinktuvas
import traukinys
#  https://docs.python.org/3.5/library/unittest.html
#  https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/

class TestPridetasLokomotyvas(unittest.TestCase):
    def test_pridetasLokomotyvas(self):
        self.assertIsNone(traukinys.Traukinys.pridetasLokomotyvas(
            traukinys.Traukinys([100, 100, 9876])))

class TestUzimtasLokomotyvas(unittest.TestCase):
    def test_uzimtasLokomotyvas(self):
        self.assertIsNone(traukinys.Traukinys.uzimtasLokomotyvas(
            traukinys.Traukinys(100, 200, 8765)))

if __name__ == '__main__':
    unittest.main()
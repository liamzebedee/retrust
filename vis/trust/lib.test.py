import unittest

from lib import *


class TestEBSL(unittest.TestCase):
    def test_opinion_add(self):
        x = (0.5, 0.2, 0.3)
        y = (0.5, 0.2, 0.3)
        z = oplus(x, y)
        print(z)
    
    def test_opinion_mult(self):
        x = (0.5, 0.2, 0.3)
        y = (0.5, 0.2, 0.3)
        z = boxtimes(x, y, func_belief_sqrt)
        print(z)


if __name__ == '__main__':
    unittest.main(
        # TestEBSL.test_opinion_add
    )

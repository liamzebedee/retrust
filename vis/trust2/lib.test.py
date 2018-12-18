import unittest

from lib import *


class TestEBSL(unittest.TestCase):
    def test_opinion(self):
        x = opinion(.5, 0, 0.5)
    
    def test_bad_opinions(self):
        with self.assertRaises(AssertionError):
            opinion(1, 0, 0)
            opinion(0, 1, 0)
            opinion(0, 0, 1)

            opinion(0.5, 0.5, 0.5)
    
    def test_to_opinion(self):
        x = to_opinion(123)
        self.assertTrue(x.sum() == 1)
    
    def test_evidence_ops(self):
        x = to_opinion(123)
        positive_ev(x)
        negative_ev(x)
        total_ev(x)
        
    def test_opinion_add(self):
        x = opinion(0.5, 0.2, 0.3)
        y = opinion(0.5, 0.2, 0.3)
        z = opinion_add(x, y)

        # self.assertEqual(
        #     z[0], 
        #     np.asarray([0.5882352941176471, 0.23529411764705882, 0.1764705882352941])
        # )
    
    def test_opinion_mult(self):
        x = opinion(0.5, 0.2, 0.3)
        y = opinion(0.5, 0.2, 0.3)
        z = opinion_mult(x, y)
        print(z)
        # [0.44473537304527666, 0.17789414921811067, 0.3773704777366128]
        # array([0.44473537, 0.17789415, 0.37737048])
    
    def test_opinion_scalar_mult(self):
        x = opinion(0.5, 0.2, 0.3)
        op = opinion_scalar_mult(2.4, x)
        self.assertEqual(op.sum(), 1)
    

class TestInteractionEngine(unittest.TestCase):
    def test_engine_blank(self):
        eng = InteractionsEngine()

        with self.assertRaises(Exception):
            u = eng.get_users()

        e = eng.get_evidence()
        self.assertLess(len(e), 1)

    
    def test_engine_inserts(self):
        eng = InteractionsEngine()
        
        eng.insert([
            ('a', 'b', 20),
            ('a', 'b', -15),
        ])

        e = eng.get_evidence()
        u = eng.get_users()

        self.assertEqual(len(e), 1)
        self.assertEqual(len(u), 2)

class TestTrust(unittest.TestCase):
    def test_converge_worldview(self):
        R = converge_worldview([
            ('a', 'b', 20),
            ('a', 'b', -15),
            ('b', 'a', 5),
            ('b', 'a', 5),
            ('b', 'a', 5),
            ('b', 'a', 5),
        ])
        R

if __name__ == '__main__':
    unittest.main(
        # TestTrust()
        TestEBSL().test_opinion_mult()
    )

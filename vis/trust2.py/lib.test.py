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
        opinion_add(x, y)
    
    def test_opinion_mult(self):
        x = opinion(0.5, 0.2, 0.3)
        y = opinion(0.5, 0.2, 0.3)
        opinion_mult(x, y)
    
    def test_opinion_scalar_mult(self):
        x = opinion(0.5, 0.2, 0.3)
        op = opinion_scalar_mult(2.4, x)
        self.assertEqual(op.sum(), 1)
    

class TestInteractionEngine(unittest.TestCase):
    def test_engine_blank(self):
        eng = InteractionsEngine()

        u = eng.get_users()
        self.assertLess(len(u), 1)

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
        self.assertEqual(len(u[0]), 2)

if __name__ == '__main__':
    unittest.main()

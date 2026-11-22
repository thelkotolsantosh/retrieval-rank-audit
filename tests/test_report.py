import unittest
from src.report import evaluate


class Ranking(unittest.TestCase):
    rows = [{"query": "a", "ranked": ["x", "y"], "relevant": ["y", "z"]},
            {"query": "b", "ranked": [], "relevant": ["z"]}]

    def test_macro_average(self):
        self.assertEqual(evaluate(self.rows, 2), dict(queries=2, k=2, recall=.25, mrr=.25))

    def test_cutoff(self):
        self.assertEqual(evaluate(self.rows, 1)["recall"], 0)

    def test_duplicate_queries(self):
        with self.assertRaises(ValueError):
            evaluate(self.rows * 2, 2)

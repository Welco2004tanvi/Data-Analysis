import unittest
import pandas as pd
from analysis import clean_data

class TestMovieAnalysis(unittest.TestCase):
    def test_clean_data_removes_nulls_and_negatives(self):
        sample_data = pd.DataFrame({
            'Title': ['A', 'B', None],
            'Rating': [7.5, -1, 8.0],
            'Genre': ['Drama', 'Comedy', 'Sci-Fi'],
            'Year': [2000, 2001, 2002]
        })
        cleaned = clean_data(sample_data)
        self.assertEqual(len(cleaned), 1)
        self.assertTrue((cleaned['Rating'] > 0).all())
        self.assertFalse(cleaned.isnull().values.any())

if __name__ == '__main__':
    unittest.main()

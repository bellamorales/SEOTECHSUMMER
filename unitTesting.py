import unittest
from filename import get_date, get_tweets


class UnitTesting(unittest.TestCase):
    def test_get_date(self):
        # tests with date 2022-07-03 is entered
        self.assertEqual(str(get_date()), "2022-07-03")

    def test_get_tweets(self):
        self.assertNotEqual(get_tweets(), None)
        self.assertTrue(len(get_tweets()) != 0)


if __name__ == '__main__':
    unittest.main()

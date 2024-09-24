import unittest
from src.basic import FirstProgram




class MyTestCase(unittest.TestCase):
    def test_something(self):
        val = FirstProgram.add(10, 20)
        self.assertEqual(val, 30)  # add assertion here


if __name__ == '__main__':
    unittest.main()

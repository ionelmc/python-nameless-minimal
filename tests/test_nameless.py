import unittest

from nameless import main


class MainTestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main([]), 0)

if __name__ == '__main__':
    unittest.main()
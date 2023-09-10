import unittest

from pypulse import Window

# Test class
class TestAddition(unittest.TestCase):

    def test_window(self):
        Window.Load()

if __name__ == '__main__':
    unittest.main()

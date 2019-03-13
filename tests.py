import unittest

from drawing.tests.test_example import ExampleCanvasTest


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(ExampleCanvasTest))

    return s


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

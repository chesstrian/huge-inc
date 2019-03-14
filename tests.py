import unittest

from drawing.tests.test_canvas_example import CanvasExampleTest
from drawing.tests.test_command_example import CommandExampleTest
from drawing.tests.test_create_line import CreateLineTest
from drawing.tests.test_create_rect import CreateRectTest


def suite():
    _suite = unittest.TestSuite()

    _suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CreateLineTest))
    _suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CreateRectTest))
    _suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CanvasExampleTest))
    _suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CommandExampleTest))

    return _suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

from unittest import TestCase

from drawing import CanvasEditor


class CreateLineTest(TestCase):
    horizontal = '------\n' \
                 '|    |\n' \
                 '| xxx|\n' \
                 '|    |\n' \
                 '|    |\n' \
                 '------'

    vertical = '------\n' \
               '| x  |\n' \
               '| x  |\n' \
               '| x  |\n' \
               '|    |\n' \
               '------'

    def test_line_left_to_right(self):
        c = CanvasEditor()
        c.create_canvas(4, 4)
        c.create_line(2, 2, 4, 2)

        self.assertEqual(c.__str__(), self.horizontal)

    def test_line_right_to_left(self):
        c = CanvasEditor()
        c.create_canvas(4, 4)
        c.create_line(4, 2, 2, 2)

        self.assertEqual(c.__str__(), self.horizontal)

    def test_line_top_to_bottom(self):
        c = CanvasEditor()
        c.create_canvas(4, 4)
        c.create_line(2, 1, 2, 3)

        self.assertEqual(c.__str__(), self.vertical)

    def test_line_bottom_to_top(self):
        c = CanvasEditor()
        c.create_canvas(4, 4)
        c.create_line(2, 3, 2, 1)

        self.assertEqual(c.__str__(), self.vertical)

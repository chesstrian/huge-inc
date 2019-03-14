from unittest import TestCase

from drawing import CanvasEditor


class CreateRectTest(TestCase):
    rectangle = '------\n' \
                '|    |\n' \
                '| xxx|\n' \
                '| x x|\n' \
                '| xxx|\n' \
                '------'

    def test_rect_top_left_to_bottom_right(self):
        c = CanvasEditor()
        c.create_canvas(4, 4)
        c.create_rectangle(2, 2, 4, 4)

        self.assertEqual(c.__str__(), self.rectangle)

    def test_rect_bottom_left_to_top_right(self):
        c = CanvasEditor()
        c.create_canvas(4, 4)
        c.create_rectangle(2, 4, 4, 2)

        self.assertEqual(c.__str__(), self.rectangle)

    def test_rect_top_right_to_bottom_left(self):
        c = CanvasEditor()
        c.create_canvas(4, 4)
        c.create_rectangle(4, 2, 2, 4)

        self.assertEqual(c.__str__(), self.rectangle)

    def test_rect_bottom_right_to_top_left(self):
        c = CanvasEditor()
        c.create_canvas(4, 4)
        c.create_rectangle(4, 4, 2, 2)

        self.assertEqual(c.__str__(), self.rectangle)

    def test_rect_same_point(self):
        c = CanvasEditor()
        c.create_canvas(2, 2)
        c.create_rectangle(2, 2, 2, 2)

        result = '----\n' \
                 '|  |\n' \
                 '| x|\n' \
                 '----'

        self.assertEqual(c.__str__(), result)

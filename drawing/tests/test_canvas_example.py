from unittest import TestCase

from drawing import CanvasEditor, CanvasNotCreatedException, InvalidLineException, OutOfRangeException


class CanvasExampleTest(TestCase):

    def test_canvas_example_output(self):
        outputs = []
        with open('drawing/tests/fixtures/output.txt', 'r') as f:
            lines = f.readlines()

            output = True  # In order to run first time
            while output:
                o_len = len(outputs)
                output = lines[6 * o_len:(o_len + 1) * 6]

                outputs.append(''.join(output))

        c = CanvasEditor()

        c.create_canvas(20, 4)
        self.assertEqual(c.__str__() + '\n', outputs[0])

        c.create_line(1, 2, 6, 2)
        self.assertEqual(c.__str__() + '\n', outputs[1])

        c.create_line(6, 3, 6, 4)
        self.assertEqual(c.__str__() + '\n', outputs[2])

        c.create_rectangle(16, 1, 20, 3)
        self.assertEqual(c.__str__() + '\n', outputs[3])

        c.bucket_fill(10, 3, 'o')
        self.assertEqual(c.__str__(), outputs[4])

    def test_canvas_not_created_exception(self):
        c = CanvasEditor()

        self.assertRaises(CanvasNotCreatedException, c.create_line, *(1, 2, 6, 2))
        self.assertRaises(CanvasNotCreatedException, c.create_rectangle, *(16, 1, 20, 3))
        self.assertRaises(CanvasNotCreatedException, c.bucket_fill, *(10, 3, 'c'))

    def test_not_horizontal_nor_vertical_line(self):
        c = CanvasEditor()
        c.create_canvas(20, 4)

        self.assertRaises(InvalidLineException, c.create_line, *(1, 3, 6, 2))

    def test_out_of_canvas(self):
        c = CanvasEditor()
        c.create_canvas(20, 4)
        c.create_line(1, 2, 6, 2)

        self.assertRaises(OutOfRangeException, c.create_line, *(21, 3, 6, 2))
        self.assertRaises(OutOfRangeException, c.create_line, *(1, 3, 6, 5))
        self.assertRaises(OutOfRangeException, c.bucket_fill, *(1, 5, 'o'))

    def test_not_fill(self):
        c = CanvasEditor()
        c.create_canvas(20, 4)
        c.create_line(1, 2, 6, 2)

        before = c.__str__()
        c.bucket_fill(3, 2, 'o')
        after = c.__str__()

        self.assertEqual(before, after)

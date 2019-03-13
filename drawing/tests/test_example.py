from unittest import TestCase

from drawing import CanvasEditor, CanvasNotCreatedException


class ExampleCanvasTest(TestCase):

    def test_example_input_example_output(self):
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
        self.assertRaises(CanvasNotCreatedException, c.create_rectangle, *(116, 1, 20, 3))
        self.assertRaises(CanvasNotCreatedException, c.bucket_fill, *(10, 3, 'c'))

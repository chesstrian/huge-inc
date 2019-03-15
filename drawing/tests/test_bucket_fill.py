from unittest import TestCase

from drawing import CanvasEditor


class BucketFillTest(TestCase):

    def test_bucket_fill_line(self):
        canvas = CanvasEditor()
        canvas.create_canvas(11, 6)
        canvas.create_line(6, 1, 6, 3)
        canvas.create_line(1, 6, 6, 6)
        canvas.bucket_fill(6, 2, '*')
        canvas.bucket_fill(6, 6, '+')

        result = '-------------\n' \
                 '|     *     |\n' \
                 '|     *     |\n' \
                 '|     *     |\n' \
                 '|           |\n' \
                 '|           |\n' \
                 '|++++++     |\n' \
                 '-------------'
        self.assertEqual(canvas.__str__(), result)

    def test_bucket_fill_rectangle(self):
        canvas = CanvasEditor()
        canvas.create_canvas(11, 6)
        canvas.create_rectangle(3, 2, 9, 5)
        canvas.bucket_fill(3, 2, '*')

        result = '-------------\n' \
                 '|           |\n' \
                 '|  *******  |\n' \
                 '|  *     *  |\n' \
                 '|  *     *  |\n' \
                 '|  *******  |\n' \
                 '|           |\n' \
                 '-------------'
        self.assertEqual(canvas.__str__(), result)

    def test_bucket_fill_line_and_rectangle(self):
        canvas = CanvasEditor()
        canvas.create_canvas(11, 6)
        canvas.create_line(6, 1, 6, 3)
        canvas.create_rectangle(3, 2, 9, 5)
        canvas.bucket_fill(3, 2, '*')

        result = '-------------\n' \
                 '|     *     |\n' \
                 '|  *******  |\n' \
                 '|  *  *  *  |\n' \
                 '|  *     *  |\n' \
                 '|  *******  |\n' \
                 '|           |\n' \
                 '-------------'
        self.assertEqual(canvas.__str__(), result)

    def test_bucket_fill_two_rectangles(self):
        canvas = CanvasEditor()
        canvas.create_canvas(11, 6)
        canvas.create_rectangle(3, 2, 9, 5)
        canvas.create_rectangle(5, 1, 7, 6)
        canvas.bucket_fill(3, 2, '*')

        result = '-------------\n' \
                 '|    ***    |\n' \
                 '|  *******  |\n' \
                 '|  * * * *  |\n' \
                 '|  * * * *  |\n' \
                 '|  *******  |\n' \
                 '|    ***    |\n' \
                 '-------------'
        self.assertEqual(canvas.__str__(), result)

    def test_bucket_fill_twice(self):
        canvas = CanvasEditor()
        canvas.create_canvas(11, 6)
        canvas.create_rectangle(1, 1, 11, 6)
        canvas.bucket_fill(3, 2, '=')

        first_result = '-------------\n' \
                       '|xxxxxxxxxxx|\n' \
                       '|x=========x|\n' \
                       '|x=========x|\n' \
                       '|x=========x|\n' \
                       '|x=========x|\n' \
                       '|xxxxxxxxxxx|\n' \
                       '-------------'
        self.assertEqual(canvas.__str__(), first_result)

        canvas.create_line(6, 2, 6, 5)
        canvas.bucket_fill(7, 2, '^')

        second_result = '-------------\n' \
                        '|xxxxxxxxxxx|\n' \
                        '|x====x^^^^x|\n' \
                        '|x====x^^^^x|\n' \
                        '|x====x^^^^x|\n' \
                        '|x====x^^^^x|\n' \
                        '|xxxxxxxxxxx|\n' \
                        '-------------'
        self.assertEqual(canvas.__str__(), second_result)

from drawing.exceptions import CanvasNotCreatedException, OutOfRangeException, InvalidLineException, InvalidCanvasSize


class CanvasEditor(object):
    """Canvas handler, low level of operations.
    """

    def __init__(self):
        self.width = self.height = None

        self.canvas = []

    def create_canvas(self, width, height):
        """Create empty canvas

        :param width: Canvas width
        :param height: Canvas height
        """
        if width < 1 or height < 1:
            raise InvalidCanvasSize('Invalid size for canvas')

        self.width = width
        self.height = height

        self.canvas = []

        for i in range(self.height + 2):
            if i in (0, self.height + 1):
                self.canvas.append(['-'] * (self.width + 2))
            else:
                self.canvas.append(['|'] + [' '] * self.width + ['|'])

    def create_line(self, x1, y1, x2, y2):
        """Create a line inside canvas from P1(x1, y1) to P2(x2, y2), only horizontal and vertical lines supported.

        :param x1: First point horizontal entry
        :param y1: First point vertical entry
        :param x2: Second point horizontal entry
        :param y2: Second point vertical entry
        """
        if not self.canvas:
            raise CanvasNotCreatedException('You can only draw if a canvas has been created')

        if not (1 <= x1 <= self.width and 1 <= y1 <= self.height):
            raise OutOfRangeException('The first point is not inside the canvas')

        if not (1 <= x2 <= self.width and 1 <= y2 <= self.height):
            raise OutOfRangeException('The second point is not inside the canvas')

        if y1 == y2:  # Horizontal line
            if x2 < x1:
                self.create_line(x2, y2, x1, y1)
                return

            for i in range(x1, x2 + 1):
                self.canvas[y2][i] = 'x'
            return
        elif x1 == x2:  # Vertical line
            if y2 < y1:
                self.create_line(x2, y2, x1, y1)
                return

            for i in range(y1, y2 + 1):
                self.canvas[i][x1] = 'x'
            return

        raise InvalidLineException('Not horizontal nor vertical line')

    def create_rectangle(self, x1, y1, x2, y2):
        """Create a rectangle inside canvas. The rectangle is defined by a diagonal given by the two points received.

        :param x1: First point horizontal entry
        :param y1: First point vertical entry
        :param x2: Second point horizontal entry
        :param y2: Second point vertical entry
        """
        self.create_line(x1, y1, x2, y1)
        self.create_line(x1, y1, x1, y2)
        self.create_line(x2, y1, x2, y2)
        self.create_line(x1, y2, x2, y2)

    def bucket_fill(self, x, y, c):
        """Fill with color c all connected points to P(x, y) with the same color.

        :param x: Seek point horizontal entry
        :param y: Seek point vertical entry
        :param c: Color to fill with
        """
        if not self.canvas:
            raise CanvasNotCreatedException('You can only draw if a canvas has been created.')

        if not (1 <= x <= self.width and 1 <= y <= self.height):
            raise OutOfRangeException('The seek is not inside the canvas')

        current_color = self.canvas[y][x]
        if current_color == c:
            return

        points = set()
        points.add((x, y))

        while points:
            x, y = points.pop()
            right = left = x

            while self._is_fillable(left, y, current_color):
                left -= 1

            while self._is_fillable(right, y, current_color):
                right += 1

            for i in range(left + 1, right):
                self.canvas[y][i] = c

                top = y + 1
                bottom = y - 1

                if self._is_fillable(i, top, current_color):
                    points.add((i, top))

                if self._is_fillable(i, bottom, current_color):
                    points.add((i, bottom))

    def _is_fillable(self, x, y, c):
        """Check if a given point P(x, y) is valid inside canvas and has color c.

        :param x: Horizontal entry
        :param y: Vertical entry
        :param c: Color, defined by a valid character
        :return: True if point is valid and has color c, False otherwise
        """
        return 1 <= x <= self.width and 1 <= y <= self.height and self.canvas[y][x] == c

    def __str__(self):
        return '\n'.join([''.join(line) for line in self.canvas])

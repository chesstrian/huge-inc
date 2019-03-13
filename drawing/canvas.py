from drawing.exceptions import CanvasNotCreatedException, OutOfRangeException, InvalidLineException


class CanvasEditor(object):
    width = None
    height = None

    canvas = None

    def create_canvas(self, width, height):
        self.width = width
        self.height = height

        self.canvas = []

        for i in range(self.height + 2):
            if i in (0, self.height + 1):
                self.canvas.append(['-'] * (self.width + 2))
            else:
                self.canvas.append(['|'] + [' '] * self.width + ['|'])

    def create_line(self, x1, y1, x2, y2):
        if not self.canvas:
            raise CanvasNotCreatedException('You can only draw if a canvas has been created')

        if not (1 <= x1 <= self.width and 1 <= y1 <= self.height):
            raise OutOfRangeException('The first point is not inside the canvas')

        if not (1 <= x2 <= self.width and 1 <= y2 <= self.height):
            raise OutOfRangeException('The second point is not inside the canvas')

        if y1 == y2:  # Horizontal line
            for i in range(x1, x2 + 1):
                self.canvas[y2][i] = 'x'
            return
        elif x1 == x2:  # Vertical line
            for i in range(y1, y2 + 1):
                self.canvas[i][x1] = 'x'
            return

        raise InvalidLineException('Not horizontal nor vertical line')

    def create_rectangle(self, x1, y1, x2, y2):
        self.create_line(x1, y1, x2, y1)
        self.create_line(x1, y1, x1, y2)
        self.create_line(x2, y1, x2, y2)
        self.create_line(x1, y2, x2, y2)

    def bucket_fill(self, x, y, c):
        if not self.canvas:
            raise CanvasNotCreatedException('You can only draw if a canvas has been created.')

        if not (1 <= x <= self.width and 1 <= y <= self.height):
            return

        if self.canvas[y][x] in ('-', '|', 'x', c):
            return

        self.canvas[y][x] = c

        self.bucket_fill(x - 1, y, c)
        self.bucket_fill(x + 1, y, c)
        self.bucket_fill(x, y - 1, c)
        self.bucket_fill(x, y + 1, c)

    def render_canvas(self):
        print(self.__str__())

    def __str__(self):
        return '\n'.join([''.join(line) for line in self.canvas])

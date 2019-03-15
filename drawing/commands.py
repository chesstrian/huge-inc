from drawing import InvalidArgumentsException, UnsupportedCommandException, CanvasNotCreatedException


class BaseCommand(object):
    """Abstract class for canvas operation commands
    """

    def __init__(self, canvas, letter, *args):
        """

        :param canvas: Canvas class instance to work with
        :param letter: Letter to define command
        :param args: Array of command arguments
        """
        self.canvas = canvas

        self.letter = letter
        self.arguments = list(map(self._cast_argument_to_int, args))

    def validate(self):
        """Method to check arguments
        """
        raise NotImplementedError

    def run(self):
        """Method to call canvas operation related to command
        """
        raise NotImplementedError

    @staticmethod
    def _cast_argument_to_int(value):
        """Private method to cast a value to integer, if not possible, same value is returned

        :param value: Value to convert to integer
        :return: Cast of value to integer if possible, value otherwise
        """
        try:
            return int(value)
        except ValueError:
            return value


class CreateCanvasCommand(BaseCommand):
    """Implement command: C w h
    w is width and h is height
    """

    def __init__(self, canvas, *args):
        super(CreateCanvasCommand, self).__init__(canvas, 'C', *args)

    def validate(self):
        if len(self.arguments) != 2:
            raise InvalidArgumentsException('Invalid number of arguments')

        if not (type(self.arguments[0]) is int and type(self.arguments[1]) is int):
            raise InvalidArgumentsException('Invalid argument type')

        if not (self.arguments[0] > 0 and self.arguments[1] > 0):
            raise InvalidArgumentsException('Invalid canvas size')

    def run(self):
        self.validate()
        self.canvas.create_canvas(*self.arguments)


class CreateLineCommand(BaseCommand):
    """Implement command: L x1 y1 x2 y2
    """

    def __init__(self, canvas, *args):
        super(CreateLineCommand, self).__init__(canvas, 'L', *args)

    def validate(self):
        if not self.canvas.canvas:
            raise CanvasNotCreatedException('You can only draw if a canvas has been created')

        if len(self.arguments) != 4:
            raise InvalidArgumentsException('Invalid number of arguments')

        for argument in self.arguments:
            if type(argument) is not int:
                raise InvalidArgumentsException('Invalid argument type')

        for i in range(4):
            if i % 2 == 0 and not (1 <= self.arguments[i] <= self.canvas.width):
                raise InvalidArgumentsException('Invalid argument value')

            if i % 2 == 1 and not (1 <= self.arguments[i] <= self.canvas.height):
                raise InvalidArgumentsException('Invalid argument value')

    def run(self):
        self.validate()
        self.canvas.create_line(*self.arguments)


class CreateRectangleCommand(BaseCommand):
    """Implement command: R x1 y1 x2 y2
    """

    def __init__(self, canvas, *args):
        super(CreateRectangleCommand, self).__init__(canvas, 'R', *args)

    def validate(self):
        if not self.canvas.canvas:
            raise CanvasNotCreatedException('You can only draw if a canvas has been created')

        if len(self.arguments) != 4:
            raise InvalidArgumentsException('Invalid number of arguments')

        for argument in self.arguments:
            if type(argument) is not int:
                raise InvalidArgumentsException('Invalid argument type')

        for i in range(4):
            if i % 2 == 0 and not (1 <= self.arguments[i] <= self.canvas.width):
                raise InvalidArgumentsException('Invalid argument value')

            if i % 2 == 1 and not (1 <= self.arguments[i] <= self.canvas.height):
                raise InvalidArgumentsException('Invalid argument value')

    def run(self):
        self.validate()
        self.canvas.create_rectangle(*self.arguments)


class BucketFillCommand(BaseCommand):
    """Implement command: B x y c
    """

    def __init__(self, canvas, *args):
        super(BucketFillCommand, self).__init__(canvas, 'B', *args)

    def validate(self):
        if not self.canvas.canvas:
            raise CanvasNotCreatedException('You can only draw if a canvas has been created')

        if len(self.arguments) != 3:
            raise InvalidArgumentsException('Invalid number of arguments')

        if not (type(self.arguments[0]) is int and type(self.arguments[1]) is int):
            raise InvalidArgumentsException('Invalid argument type')

        if type(self.arguments[2]) is not str:
            raise InvalidArgumentsException('Invalid argument type')

        if not (1 <= self.arguments[0] <= self.canvas.width):
            raise InvalidArgumentsException('Invalid argument value')

        if not (1 <= self.arguments[1] <= self.canvas.height):
            raise InvalidArgumentsException('Invalid argument value')

    def run(self):
        self.validate()
        self.canvas.bucket_fill(*self.arguments)


class PrintCommand(BaseCommand):
    """Command not asked in requirements, implemented only for tool usability purposes with stdin/stdout
    """

    def __init__(self, canvas):
        super(PrintCommand, self).__init__(canvas, 'P')

    def validate(self):
        pass

    def run(self):
        print(self.canvas.__str__())


def run_command(canvas, line, render=True):
    """Method to run operations from file or stdin

    :param canvas: Canvas instance to work with
    :param line: Command from input
    :param render: Optional parameter used to print, required to avoid prints in tests
    """
    line = line.split(' ')
    letter = line.pop(0)

    if letter == 'C':
        CreateCanvasCommand(canvas, *line).run()
    elif letter == 'L':
        CreateLineCommand(canvas, *line).run()
    elif letter == 'R':
        CreateRectangleCommand(canvas, *line).run()
    elif letter == 'B':
        BucketFillCommand(canvas, *line).run()
    else:
        raise UnsupportedCommandException('Unsupported command!')

    if render:
        PrintCommand(canvas).run()

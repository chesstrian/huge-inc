from drawing import InvalidArgumentsException, UnsupportedCommandException


class Command(object):

    def __init__(self, canvas, letter, *args):
        self.canvas = canvas

        self.letter = letter
        self.arguments = map(self._cast_argument_to_int, args)

    def validate(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    @staticmethod
    def _cast_argument_to_int(value):
        try:
            return int(value)
        except ValueError:
            return value


class CreateCanvasCommand(Command):

    def __init__(self, canvas, *args):
        super(CreateCanvasCommand, self).__init__(canvas, 'C', *args)

    def validate(self):
        if len(self.arguments) != 2:
            raise InvalidArgumentsException('Invalid number of arguments')

        if not (type(self.arguments[0]) is int and type(self.arguments[1]) is int):
            raise InvalidArgumentsException('Invalid argument type')

        if not (self.arguments[0] > 1 and self.arguments[1] > 1):
            raise InvalidArgumentsException('Invalid canvas size')

    def run(self):
        self.validate()
        self.canvas.create_canvas(*self.arguments)


class CreateLineCommand(Command):

    def __init__(self, canvas, *args):
        super(CreateLineCommand, self).__init__(canvas, 'L', *args)

    def validate(self):
        pass

    def run(self):
        self.validate()
        self.canvas.create_line(*self.arguments)


class CreateRectangleCommand(Command):

    def __init__(self, canvas, *args):
        super(CreateRectangleCommand, self).__init__(canvas, 'R', *args)

    def validate(self):
        pass

    def run(self):
        self.validate()
        self.canvas.create_rectangle(*self.arguments)


class BucketFillCommand(Command):

    def __init__(self, canvas, *args):
        super(BucketFillCommand, self).__init__(canvas, 'B', *args)

    def validate(self):
        pass

    def run(self):
        self.validate()
        self.canvas.bucket_fill(*self.arguments)


class PrintCommand(Command):

    def __init__(self, canvas):
        super(PrintCommand, self).__init__(canvas, 'P')

    def validate(self):
        pass

    def run(self):
        print(self.canvas.__str__())


def run_command(canvas, line, render=True):
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

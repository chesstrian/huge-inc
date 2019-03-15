from unittest import TestCase

from drawing import CanvasEditor, InvalidArgumentsException, run_command, UnsupportedCommandException, \
    CanvasNotCreatedException
from drawing.commands import Command, CreateCanvasCommand, CreateLineCommand, CreateRectangleCommand, BucketFillCommand


# noinspection PyAbstractClass
class ChildCommand(Command):
    pass


class CommandExceptionTest(TestCase):

    def test_not_implemented_error(self):
        canvas = CanvasEditor()
        command = ChildCommand(canvas, 'T')

        self.assertRaises(NotImplementedError, command.validate)
        self.assertRaises(NotImplementedError, command.run)

    def test_create_canvas_invalid_argument(self):
        canvas = CanvasEditor()

        command = CreateCanvasCommand(canvas, *(1,))
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = CreateCanvasCommand(canvas, *(1, 'a'))
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = CreateCanvasCommand(canvas, *(1, -1))
        self.assertRaises(InvalidArgumentsException, command.validate)

    def test_create_line_invalid_argument(self):
        canvas = CanvasEditor()

        command = CreateLineCommand(canvas, *(1,))
        self.assertRaises(CanvasNotCreatedException, command.validate)

        CreateCanvasCommand(canvas, *(4, 4)).run()
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = CreateLineCommand(canvas, *(1, 'a', 2, 3))
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = CreateLineCommand(canvas, *(-1, 1, 2, 3))
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = CreateLineCommand(canvas, *(1, -1, 2, 3))
        self.assertRaises(InvalidArgumentsException, command.validate)

    def test_create_rect_invalid_argument(self):
        canvas = CanvasEditor()

        command = CreateRectangleCommand(canvas, *(1,))
        self.assertRaises(CanvasNotCreatedException, command.validate)

        CreateCanvasCommand(canvas, *(4, 4)).run()
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = CreateRectangleCommand(canvas, *(1, 'a', 2, 3))
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = CreateRectangleCommand(canvas, *(-1, 1, 2, 3))
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = CreateRectangleCommand(canvas, *(1, -1, 2, 3))
        self.assertRaises(InvalidArgumentsException, command.validate)

    def test_bucket_fill_invalid_argument(self):
        canvas = CanvasEditor()

        command = BucketFillCommand(canvas, *(1,))
        self.assertRaises(CanvasNotCreatedException, command.validate)

        CreateCanvasCommand(canvas, *(4, 4)).run()
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = BucketFillCommand(canvas, *(1, 'a', 2))
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = BucketFillCommand(canvas, *(1, 2, 2))
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = BucketFillCommand(canvas, *(-1, 1, 'c'))
        self.assertRaises(InvalidArgumentsException, command.validate)

        command = BucketFillCommand(canvas, *(1, -1, 'c'))
        self.assertRaises(InvalidArgumentsException, command.validate)

    def test_run_command_unsupported_command(self):
        canvas = CanvasEditor()

        self.assertRaises(UnsupportedCommandException, run_command, *(canvas, 'T 1 2 3'))

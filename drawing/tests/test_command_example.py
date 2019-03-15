from unittest import TestCase, mock

from drawing import CanvasEditor, run_command
from drawing.commands import PrintCommand


class CommandExampleTest(TestCase):

    def test_command_example_input_output(self):
        with open('drawing/tests/fixtures/input.txt', 'r') as f:
            commands = f.readlines()

        outputs = []
        with open('drawing/tests/fixtures/output.txt', 'r') as f:
            lines = f.readlines()

            output = True  # In order to run first time
            while output:
                o_len = len(outputs)
                output = lines[6 * o_len:(o_len + 1) * 6]

                outputs.append(''.join(output))

        canvas = CanvasEditor()

        length = len(commands)
        for i in range(length):
            line = commands[i]
            run_command(canvas, line, render=False)

            result = canvas.__str__()
            result += '\n' if i < length - 1 else ''

            self.assertEqual(result, outputs[i])

    def test_run_command(self):
        canvas = CanvasEditor()

        result = '---\n' \
                 '| |\n' \
                 '---'

        with mock.patch('drawing.commands.PrintCommand') as MockPrint:
            run_command(canvas, 'C 1 1')
            MockPrint.assert_called_once_with(canvas)
            self.assertEqual(canvas.__str__(), result)

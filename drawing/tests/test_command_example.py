from unittest import TestCase

from drawing import CanvasEditor, run_command


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

#!/usr/bin/env python

import argparse
import sys

from drawing import run_command, CanvasEditor, CanvasNotCreatedException, OutOfRangeException, InvalidLineException, \
    InvalidArgumentsException, UnsupportedCommandException

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command line for Drawing Tool')
    parser.add_argument('-i', '--input', help='Input file to read commands from. If no input file is given, standard '
                                              'input is expected.')
    parser.add_argument('-o', '--output', help='Output file to write results to. If no output file is given, results '
                                               'will be printed to standard output')
    args = parser.parse_args()

    if (args.input and not args.output) or (args.output and not args.input):
        parser.error('Input and Output have to be both file or standard')

    canvas = CanvasEditor()

    if args.input:  # and args.output
        with open(args.input) as file_input:
            file_output = open(args.output, 'a')
            sys.stdout = file_output

            for line in file_input.readlines():
                run_command(canvas, line)

            file_output.close()
    else:
        line = input('> ')
        while line not in ('q', 'quit', 'exit'):
            try:
                run_command(canvas, line)
            except (CanvasNotCreatedException, OutOfRangeException, InvalidLineException, InvalidArgumentsException,
                    UnsupportedCommandException) as e:
                print(e.message)

            line = input('> ')

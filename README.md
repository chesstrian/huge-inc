# Huge Inc
_Code Challenge_

Demo app for Huge Inc's code challenge.

Solution developed in Python 

## Run Tests

* `python -m unittest discover drawing/tests/`

## Code coverage

* `pip install coverage`
* `coverage run main.py -i input/input.txt -o input/output.txt`
* `coverage report -m`

## Run Project

* `python main.py -h` or `python main.py --help` to see options.
* `python main.py` to write commands in standard input.
* `python main.py --input input/input.txt --output ~/output.txt` to read commands from a file and print output to 
another file.

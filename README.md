# Huge Inc
_Code Challenge_

Demo app for Huge Inc's code challenge. Solution developed in Python 3.

## Environment Setup

* `virtualenv -p python3 envpy3`
* `source envpy3/bin/activate`

## Run Tests

* `python tests.py`

## Test Coverage

* `pip3 install coverage`
* `coverage run tests.py`
* `coverage report -m`

## Run Project

* `python main.py -h` or `python main.py --help` to see options.
* `python main.py` to write commands in standard input.
* `python main.py --input input/input.txt --output ~/output.txt` to read commands from a file and print output to 
another file.

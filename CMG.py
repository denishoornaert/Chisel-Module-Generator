"""
Usage: CMG.py (-m MODULE) [-p PACKAGE]

Process FILE and optionally apply correction to either left-hand side or
right-hand side.

Arguments:
  MODULE    optional input file
  PACKAGE   correction angle, needs FILE, --left or --right to be present

Options:
  -h --help
  -m MODULE     The name of the module to be generated
  -p PACKAGE    The name of the package in which the module will be placed
"""
from docopt import docopt


if (__name__ == '__main__'):
    arguments = docopt(__doc__)
    if(arguments['-p'] == None ):
        arguments['-p'] = arguments['-m'].lower()
    print(arguments)

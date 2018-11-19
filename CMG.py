"""
Usage: CMG.py (-m MODULE) [-p PACKAGE]

Process FILE and optionally apply correction to either left-hand side or
right-hand side.

Arguments:
  MODULE                Mandatory input file
  PACKAGE               Correction angle, needs FILE, --left or --right to be present
  PATH                  Path to the future files location
  TESTPATH              Path to the future test files location

Options:
  -h --help
  -m MODULE             The name of the module to be generated
  -p PACKAGE            The name of the package in which the module will be placed
"""
import os
from docopt import docopt

TEMPLATE_PATH = "templates/"
DEFAULT_PATH = "src/main/scala/"
DEFAULT_TEST_PATH = "src/test/scala"
EXTENSION = "scala"

def replace(packageName, moduleName, template):
    template = template.replace("<?@package@?>", packageName)
    template = template.replace("<?@module@?>", packageName)
    return template

def read(fileName):
    readFile = open(TEMPLATE_PATH+fileName, "r")
    content = readFile.read()
    readFile.close()
    return content

def write(fileName, content):
    writeFile = open(DEFAULT_PATH+"/"+fileName+"."+EXTENSION, "w")
    writeFile.write(content)
    writeFile.close()

def readReplaceWrite(templateFile, packageName, moduleName):
    content = read(templateFile)
    content = replace(packageName, moduleName, content)
    write(moduleName, content)

def manageArgs():
    args = docopt(__doc__)
    if(arguments['-p'] == None ):
        arguments['-p'] = arguments['-m'].lower()
    return args

if (__name__ == '__main__'):
    args = manageArgs()
    print(args)
    # --------------------------------------------------------------------------
    templateFiles = os.listdir(TEMPLATE_PATH)
    for file in templateFiles:
        readReplaceWrite(file, args['-p'], args['-m'])

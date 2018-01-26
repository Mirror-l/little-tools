"""autopep8_dir

Usage:
  autopep8_dir <dir>

Options:
  -h --help     Show this screen.
  --version     Show version.
"""


import os
import sys
import autopep8
from docopt import docopt


def format(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            if fullpath.endswith('.py'):
                with open(fullpath, 'r') as rf:
                    fixed_code = autopep8.fix_code(rf.read())
                    with open(fullpath, 'w') as wf:
                        wf.write(fixed_code)


def main():
    arguments = docopt(__doc__, version='atuopep8-dir 0.0.1')
    print(arguments)
    path = arguments['<dir>']
    if not os.path.exists(path) or not os.path.isdir(path):
        print('Not such dir or the path is file')
    format(path)
    print('done')


if __name__ == '__main__':
    sys.exit(main())

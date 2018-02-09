"""template

Usage:
  template -if <inputfile> -of <outputfile> -v <varsfile>

Options:
  -h --help     Show this screen.
  --version     Show version.
  -if           input file
  -of           output file
  -v            varsfile
"""
import json
import sys
from jinja2 import Template
from docopt import docopt


def read_from_file(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def write_to_file(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)


def main():
    arguments = docopt(__doc__, version='distribute_pubkey 0.0.1')
    inputfile = arguments['<inputfile>']
    outputfile = arguments['<outputfile>']
    varsfile = arguments['<varsfile>']
    template = Template(read_from_file(inputfile))
    content = template.render(**json.load(open(varsfile)))
    write_to_file(outputfile, content)

if __name__ == '__main__':
    sys.exit(main())

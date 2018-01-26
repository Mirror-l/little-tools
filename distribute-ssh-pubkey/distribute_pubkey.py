"""
Usage:
  distribute_pubkey -f <filepath>
"""
import sh
import os
import sys
from docopt import docopt


class PubkeyTool(object):
    def __init__(self, algorithm='rsa',
                 direct=os.path.expanduser('~')+'/.ssh',
                 key_password=''):
        self.algorithm = algorithm
        self.filepath = direct+'/id_{}'.format(algorithm)
        self.key_password = key_password
        self.pubkey_path = direct+'/id_{}.pub'.format(algorithm)

    def generate_pubkey(self):
        if not os.path.exists(self.filepath):
            sh.ssh_keygen('-t', self.algorithm, '-P',
                          self.key_password, '-f', self.filepath)

    def distribute_pubkey(self, confs=[]):
        for x in confs:
            port = 22
            url, password = x[0], x[1]
            if ':' in url:
                url, port = url.split(':')
            sh.sshpass('-p', password, 'ssh-copy-id', '-i', self.pubkey_path,
                       url, '-p', port, '-o', 'StrictHostKeyChecking no')


def load_file(filepath):
    result = []
    with open(filepath) as f:
        line = f.readline()
        while line:
            l = line.strip().split(' ')
            if len(l) != 2:
                line = f.readline()
                continue
            result.append(tuple(l))
            line = f.readline()
    return result


def main():
    arguments = docopt(__doc__, version='distribute_pubkey 0.0.1')
    path = arguments['<filepath>']
    conf = load_file(path)
    tool = PubkeyTool()
    tool.generate_pubkey()
    tool.distribute_pubkey(conf)


if __name__ == '__main__':
    sys.exit(main())

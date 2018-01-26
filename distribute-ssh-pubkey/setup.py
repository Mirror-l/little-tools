from setuptools import setup


setup(name='distribute-ssh-pubkey',
      version='0.0.1',
      description='一键分发ssh公钥',
      author='Stcoder',
      author_email='stcode98@foxmail.com',
      py_modules=['distribute_pubkey'],
      install_requires=['sh', 'docopt'],
      entry_points={'console_scripts': [
          'distribute_pubkey = distribute_pubkey:main']},
      zip_safe=False,
      license='MIT'
      )

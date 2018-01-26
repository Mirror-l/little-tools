from setuptools import setup


setup(name='autopep8-dir',
      version='0.0.1',
      description='autopep8格式化整个文件夹的工具',
      author='Stcoder',
      author_email='stcode98@foxmail.com',
      py_modules=['autopep8_dir'],
      install_requires=['autopep8', 'docopt'],
      entry_points={'console_scripts': ['autopep8_dir = autopep8_dir:main']},
      zip_safe=False,
      license='MIT'
      )

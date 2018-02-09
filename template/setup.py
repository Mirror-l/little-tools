from setuptools import setup


setup(name='template',
      version='0.0.1',
      description='用于填充模板,从而修改文档的常修改项',
      author='Stcoder',
      author_email='stcode98@foxmail.com',
      py_modules=['template'],
      install_requires=['jinja2', 'docopt'],
      entry_points={'console_scripts': [
          'template = template:main']},
      zip_safe=False,
      license='MIT'
      )

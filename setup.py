from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-CP_Steps',
      version='0.0.2',
      description='CraftBeerPi4 Step Plugin',
      author='Juliano Real',
      author_email='real.juliano@gmail.com',
      url='',
      include_package_data=True,
      license='GPLv3',
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-CP_Steps': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-CP_Steps'],
      install_requires=[
	  'numpy>=1.20',
      ],      
      long_description=long_description,
      long_description_content_type='text/markdown'
     )

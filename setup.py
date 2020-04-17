__author__ = "evfairchild"

import os

from distutils.core import setup

SCRIPT_DIR = os.path.dirname(__file__)

if not SCRIPT_DIR:
    SCRIPT_DIR = os.getcwd()

# create requirements list from requirements.txt
install_requirements = []
with open(os.path.join(SCRIPT_DIR, 'requirements.txt')) as file:
    for line in file.readlines():
        if line.startswith('-'):
            continue

        install_requirements.append(line.strip())

# add NYT datafiles to 'files' directory
data_files = [(dirpath, [os.path.join(dirpath, x) for x in filenames])
              for dirpath, dirnames, filenames in os.walk('files') if filenames]


setup(name="crossword",
      version='0.0.1',
      description='Web Based Crossword puzzle game.',
      author='Evan Fairchild',
      author_email='evfairchild@gmail.com',
      packages=[],
      scripts=[],
      data_files=data_files,
      long_description=open('README.md').read,
      url='https://github.com/evfairchild/crossword',
      install_requires=install_requirements
      )

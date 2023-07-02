from setuptools import setup,find_packages
from typing import List

#declaring variables for setup functions
PROJECT_NAME='housing-predictor'
VERSION='0.0.1'
AUTHOR='Vikas Yadav'
DESCRIPTION='this is my first project'
PACKAGES=['housing']
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()-> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
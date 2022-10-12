from setuptools import setup,find_packages
from typing import List

#declaring the veriable for setup function
PROJECT_NAME= 'housing-prediction'
VERSION="0.0.4"
AUTHOR='himanshu sharma'
DESRCIPTION='This is first project of fsds'
REQUIREMENT_FILE_NAME='requirement.txt'


def get_requirements_list()->List[str]:
    '''this function return the list of requirement
    mention in the requirement.txt file'''
    with open(REQUIREMENT_FILE_NAME)as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

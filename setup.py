from setuptools import setup, find_packages

setup(
    name='aocref',
    version='1.0.2',
    description='Age of Empires reference data',
    url='https://github.com/siegeengineers/aoc-reference-data',
    packages=find_packages(),
    package_data={'aocref': [
        'data/datasets/*',
        'data/constants.json'
    ]},
)

#!/usr/bin/env python

import importlib
import setuptools

name = 'aoc_2018'


setuptools.setup(
    name=name,
    version='0.2',
    author="Matt Oztalay and Tyler Jachetta",
    author_email="me@tylerjachetta.net",
    url="www.tylerjachetta.net",
    description="Working at getting back into the swing of process in python, so doing the whole thing this year.",
    long_description="todo",
    #requires=[],
    license="MIT License",
    packages=setuptools.find_packages(),
    package_data={'': ['input/*.input']},
    entry_points = {
        'console_scripts': [
            'hello_world_aoc=aoc_2018.cli:hello_world',
            'run_day=aoc_2018.cli:run_day'
        ],
    }
)

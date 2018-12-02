#!/usr/bin/env python

import setuptools

name = 'aoc_2018'


setuptools.setup(
    name=name,
    version='0.1',
    author="Matt Oztalay and Tyler Jachetta",
    author_email="me@tylerjachetta.net",
    url="www.tylerjachetta.net",
    description="Working at getting back into the swing of process in python, so doing the whole thing this year.",
    long_description="todo",
    requires=['krpc'],
    license="MIT License",
    packages=setuptools.find_packages(),
    data_files=[],
    entry_points = {
        'console_scripts': [
            'hello_world=aoc_2018.cli:hello_world'
        ],
    }
)

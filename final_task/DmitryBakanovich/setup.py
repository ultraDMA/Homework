#!/usr/bin/env python

import sys
import setuptools
import os
sys.path.append(os.getcwd())

path_dir = sys.path[0]
sys.path.insert(1, path_dir)


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rss_reader",
    version="0.4.0",
    author="Dmitry Bakanovich",
    author_email="dbakanovich@gmail.com",
    description="Pure Python command-line RSS reader.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'rss_reader': path_dir},
    install_requires=[
        'argparse',
        'requests',
        'bs4',
        'dateparser',
        'datetime',
        'lxml',
        'xhtml2pdf'],
    packages=setuptools.find_packages(),
    includepackagedata=[],
    py_modules=['starter', 'rss_reader'],
    entry_points={
        'console_scripts': ['rss-reader=rss_reader:main_func']},
    python_requires=">=3.9",



)


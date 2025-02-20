# -*- coding: utf-8 -*-
"""setup.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uLuxB9h0zI4yxaVWY9-8cV9yQOJmkATv
"""

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'A Python package to perform TOPSIS analysis.'
LONG_DESCRIPTION = """
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a powerful multi-criteria decision-making (MCDM) method.
This Python package simplifies the TOPSIS process, allowing users to rank alternatives based on multiple criteria.

Key features include:
- Easy integration with CSV data.
- Automated ranking of alternatives.
- Clear error handling for invalid inputs.
- Customizable weights and impacts.

Analyze your data efficiently and make informed decisions with this intuitive TOPSIS package. Simply run the following command in your terminal:
python -m topsis <input_file.csv> <weights> <impacts> <result_file.csv>
"""
# Setting up
setup(
    name="Topsis-Anoushka-102203560",
    version=VERSION,
    author="Anoushka Duggal",
    author_email="duggal.anoushka@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    keywords=['python', 'topsis', 'anoushka', '102203560'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
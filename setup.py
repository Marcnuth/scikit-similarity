'''
Setup scikit-similarity
'''

from setuptools import setup, find_packages


setup(
    name='scikit-similarity',
    version='0.1.0',

    description=("similarity alogrithm tools for various data type"),

    url="https://github.com/Marcnuth/scikit-similarity",

    # Author details
    author="Marcnuth",
    author_email="marcnuth@foxmail.com",

    license="Apache License 2.0",

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3'

    ],

    # What does your project relate to?
    keywords=("similarity", "scikit", "mathematics"),

    packages=find_packages("."),

    install_requires=[
        "numpy",
        "arrow",
        "statsmodels",
        "opencv-python",
        "scikit-image"
    ],

)
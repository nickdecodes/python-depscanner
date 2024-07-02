#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : nickdecodes
@Email   : nickdecodes@163.com
@Usage   :
@FileName: setup.py
@DateTime: 2024/1/28 18:50
@SoftWare: 
"""

from setuptools import setup, find_packages


def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name='depscanner',
    version='0.4',
    keywords=['depscanner', 'python', 'dependency'],
    package_data={"": ["LICENSE", "NOTICE"]},
    include_package_data=True,
    packages=find_packages(),
    author="nickdecodes",
    author_email="nickdecodes@163.com",
    description="Python Dependency Scanner",
    long_description=readme(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[
        'requests',
        'aiohttp',
        'stdlib_list',
        'requests',
        'twine',
        'build',
        'installer'
    ],
    project_urls={
        "Documentation": "http://python-depscanner.readthedocs.io",
        "Source": "https://github.com/nickdecodes/python-depscanner",
    },
    license='Apache License 2.0'
)

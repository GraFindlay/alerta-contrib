#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import codecs
from setuptools import setup

__author__ = "Mircea Ulinic <ping@mirceaulinic.net>"
__author__ = "James Kirsch <headphonejames@gmail.com>"

with codecs.open("README.rst", "r", encoding="utf8") as file:
    long_description = file.read()

setup(
    name="alerta-blackout-regex",
    version="3.1.0",
    author="Mircea Ulinic, James Kirsch",
    author_email="headphonejames@gmail.com",
    py_modules=["blackout_regex"],
    description="Alerta Blackout enhancement plugin",
    long_description=long_description,
    include_package_data=True,
    zip_safe=True,
    url='https://github.com/G-Research/alerta-contrib',
    license="Apache License 2.0",
    entry_points={"alerta.plugins": ["blackout_regex = blackout_regex:BlackoutRegex"]},
)

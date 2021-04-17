#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- mode: python -*-
import sys
from setuptools import setup

if sys.hexversion < 0x02070000:
    raise RuntimeError("Python 2.7 or higher required")

setup(
    name="comp-neurosci-crcns-vta-1",
    version="0.0.1",
    package_dir={'comp-neurosci-crcns-vta-1': 'src'},
    packages=["comp-neurosci-crcns-vta-1"],

    description="",
    long_description="",
    install_requires=[
        "numpy>=1.10",
        "parse>=1.19",
        "pandas>=1.2",
    ],

    author="Katherine Nimchuk, Ekaterina Stepanova, Emma Whelan, Jonah Weissman",
)

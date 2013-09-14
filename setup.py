#!/usr/bin/env python

import sys
import os
from setuptools import setup


_top_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_top_dir, "lib"))
import cinii
del sys.path[0]
README = open(os.path.join(_top_dir, 'README.md')).read()

setup(name='CiNii',
    version="0.1",
    description="CiNii API wrapper for Python",
    long_description=README,
    classifiers=[c.strip() for c in """
                            Development Status :: 1 - Planning
                            Intended Audience :: Developers
                            License :: OSI Approved :: MIT License
                            Operating System :: OS Independent
                            Programming Language :: Python :: 2.7
                            Topic :: Software Development :: Libraries :: Python Modules
                            """.split('\n') if c.strip()],
    keywords='PyCiNii',
    author='syguer',
    author_email='ksk.i.530@gmail.com',
    maintainer='syguer',
    maintainer_email='ksk.i.530@gmail.com',
    url='http://github.com/syguer/PyCiNii',
    license='MIT',
    py_modules=["cinii"],
    package_dir={"": "lib"},
    include_package_data=True,
    zip_safe=False,
    )


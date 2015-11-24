#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from os import path
from codecs import open
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

import tencentyun_porndetect

install_requires = [
    'requests',
]

setup(
    name='tencentyun-porndetect',
    description='TencentYun Porndetect for Python SDK',
    long_description=long_description,
    version=tencentyun_porndetect.__version__,
    keywords=('tencentyun', 'porndetect'),
    license='MIT',
    url='https://github.com/newliver/tencentyun-prondetect',

    author='newliver',
    author_email='updatanow@gmail.com',
    packages = ['tencentyun_porndetect'],
    package_data={
        'tencentyun_porndetect': ["*.py"],
    },
    install_requires=install_requires,
)

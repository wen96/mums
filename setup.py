# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

version = __import__('mums').__version__


setup(
    name='Mums',
    version=version,
    author=u'Rubén Pardo',
    author_email='yosoyruben@gmail.com',
    packages=find_packages(),
    url='https://github.com/wen96/mums',
    license='MIT',
    description='Offer-menu app',
    include_package_data=True
)

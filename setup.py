# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

from django_settings import __version__ as version


setup(
    name='django-settings',
    version=version,
    description='Simple django reusable application for storing project settings in database.',
    author='Kuba Janoszek',
    author_email='kuba.janoszek@gmail.com',
    url='http://github.com/jqb/django-settings',
    packages=find_packages(exclude=['example*', 'tests*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=['django',],  
)


# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI


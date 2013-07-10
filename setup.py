# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


#Cannot import django_settings, because it will escalate impporting django at install time
# this escalation breaks automated virtualenv creation from requirement files
#import django_settings



setup(
    name='django-settings',
    version='1.3-3-beta',
    description='Simple django reusable application for storing project settings in database.',
    author='Kuba Janoszek',
    author_email='toni.royhy@designhouseilo.fi',
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


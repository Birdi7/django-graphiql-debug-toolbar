#!/usr/bin/env python

import os
import re

from setuptools import find_packages, setup


def get_long_description():
    for filename in ('README.rst',):
        with open(filename, 'r') as f:
            yield f.read()


def get_version(package):
    with open(os.path.join(package, '__init__.py')) as f:
        pattern = r'^__version__ = [\'"]([^\'"]*)[\'"]'
        return re.search(pattern, f.read(), re.MULTILINE).group(1)


setup(
    name='django-graphiql-debug-toolbar',
    version=get_version('graphiql_debug_toolbar'),
    license='MIT',
    description='Django Debug Toolbar for GraphiQL IDE',
    long_description='\n\n'.join(get_long_description()),
    author='mongkok',
    author_email='domake.io@gmail.com',
    maintainer='mongkok',
    url='https://github.com/flavors/django-graphiql-debug-toolbar/',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        'Django>=2.0',
        'django-debug-toolbar>=2.0',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
    ],
    zip_safe=False,
)

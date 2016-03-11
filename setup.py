#!/usr/bin/env python

from setuptools import setup, find_packages
DESCRIPTION = ("CloudVision REST API with Eve.")

install_requires = [
    'eve>=0.6',
]

try:
    from collections import OrderedDict  # noqa
except ImportError:
    # Python 2.6 needs this back-port
    install_requires.append('ordereddict')


setup(
    name='cloudvision-api',
    version='0.1',
    description=DESCRIPTION,
    author='Sam Stoelinga',
    author_email='sammiestoel@gmail.com',
    url='http://github.com/samos123/cloudvision-api',
    license='BSD',
    platforms=["any"],
    packages=find_packages(),
    test_suite="tests",
    install_requires=install_requires,
    tests_require=['redis', 'testfixtures'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

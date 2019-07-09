# -*- coding: utf-8 -*-
# Learn more: https://github.com/Conr86/PySGP30

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='pysgp30',
    description='Library for reading data from the Sensirion SGP30',
    version='0.1.6',
    long_description=readme,
    author='Connor Kneebone',
    author_email='connor@sfxrescue.com',
    url='https://github.com/Conr86/PySGP30',
    license='MIT',
    packages=find_packages(exclude=('tests')),
    install_requires=['smbus2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='sgp30 i2c smbus smbus2',
)

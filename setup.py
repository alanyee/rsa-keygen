# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='rsa-keygen',
    entry_points={
      'console_scripts': [
          'rsa-keygen = rsa:main',
      ],
    },
    version='0.0.1',
    description='Generate large textbook integer-type RSA schema',
    long_description=readme,
    author='Alan Yee',
    author_email='alanyee@users.noreply.github.com',
    url='https://github.com/alanyee/rsa-keygen',
    packages=find_packages(where='rsactf',include=('Cryptodome'),exclude=('tests', 'docs')),
    include_package_data=True,
    python_requires='>=3.8',
    extras_require={
        'normal': ['pycryptodomex'],
        'testing': ["pylint", "pytest", "mypy"]
    }
)

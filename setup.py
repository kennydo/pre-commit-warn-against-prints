import sys
from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_warn_against_prints',
    description='A pre-commit hook to warn against using prints.',
    url='https://github.com/kennydo/pre-commit-warn-against-prints',
    version='0.0.1',

    author='Kenny Do',
    author_email='chinesedewey@gmail.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'warn-against-prints = pre_commit_warn_against_prints.cli:main',
        ],
    },
)

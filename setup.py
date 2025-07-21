from setuptools import setup

long_description = open("README.md").read()

setup(
    name='insilicoq',
    version='0.1',
    description='A Python package for Quantum Computation based Drug Desgin.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Chemistry, Physics',
        'Operating System :: Windows',
        'Programming Language :: Python'
        ],
    url='https://github.com/Rajahemed/quantum',
    author='rajahemed kotekhan',
    author_email='rajahmedkotekhan3581@gmail.com',
    license='MIT',
    packages=['insilicoq'],
    install_requires=[
        'numpy',
        'pandas',
        'torch',
        'transformers',
        'sentencepiece',
        'matplotlib',
        'seaborn',
        'qiskit',
        'qiskit_machine_learning',
        'pylatexenc',
        'rdkit-pypi',
        'chembl_webresource_client',
        'pubchempy'
    ],
)

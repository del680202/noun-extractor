from setuptools import setup, find_packages

setup(
    name                = 'noun-extractor',
    version             = '0.1.0',
    description         = 'A simple tool for extracting noun from csv file',
    long_description    = open('README.md').read().strip(),
    author              = 'Terrence Chin',
    author_email        = 'del680202@gmail.com',
    url                 = 'https://github.com/del680202/noun-extractor.git',
    license             = 'BSD',
    packages            = find_packages(),
    install_requires    = ['nltk'],
    entry_points        = {
         'console_scripts': [
            'noun-extractor = nounextractor.nounextractor:main'
        ] 
    }
)

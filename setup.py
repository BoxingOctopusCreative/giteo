from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# automatically captured required modules for install_requires in requirements.txt and as well as configure dependency links
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]

dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup (
    name             = 'giteo',
    description      = 'Giteo: A CLI Client for GitHub\'s Git.io URL Shortener',
    version          = '1.0.0',
    packages         = find_packages(), # list of all packages
    install_requires = install_requires,
    python_requires  = '>=3.7', # any python greater than 3.7
    entry_points     = '''
        [console_scripts]
        giteo=giteo.__main__:giteo
    ''',
    author                        = "Ryan Draga",
    keyword                       = "git, github, url_shortener",
    long_description              = README,
    long_description_content_type = "text/markdown",
    license                       = 'Apache-2.0',
    url                           = 'https://github.com/BoxingOctopus/giteo',
    download_url                  = 'https://github.com/BoxingOctopus/giteo/archive/1.0.0.tar.gz',
    dependency_links              = dependency_links,
    author_email                  = 'ryan.draga@boxingoctop.us',
    classifiers                   = [
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
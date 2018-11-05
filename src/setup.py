import os
from codecs import open as codecs_open
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

setup(
    name="example",
    version="0.0.1",
    # The project's main homepage.
    url="https://gitlab.com/stoneid/stoneid",
    # Author details
    author="<Add your name>",
    author_email="<Add your email address>",
    # Choose your license
    license="All Rights Reserved",
    package_dir={"": "main"},
    entry_points={"console_scripts": ["db_import=assignment.main:main"]},
    install_requires=[
        "sqlalchemy==1.2.13",
        "beautifulsoup4",
        "requests"
    ],
    tests_require=[
        "pytest",
    ],
)

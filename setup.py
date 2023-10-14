"""
Setup.py file to build and install package
"""
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding='utf-8') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read(filename):
    """
    read some file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

PACKAGE_PYPI_NAME = 'django-dry-tests'
PACKAGE_NAME = "dry_tests"
PACKAGE_VERSION = "0.2.1"
DEVELOPMENT_STATUS = 'Development Status :: 3 - Alpha'

setup(
    name=PACKAGE_PYPI_NAME,
    version=PACKAGE_VERSION,
    packages=find_packages(
        include=[PACKAGE_NAME, f'{PACKAGE_NAME}.*']
    ),
    include_package_data=True,
    license="MIT",
    description="Package with new powerful TestCases and Assets "
                "to test django application fast. TDD is supported",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/quillcraftsman/django-dry-tests",
    author="quillcraftsman",
    author_email="quill@craftsman.lol",
    keywords=["django", "tests", "test-driven-development", 'asserts', 'testcases'],
    # install_requires=[
    #     'Django==4.2.6',
    # ],
    python_requires=">=3",
    classifiers=[
        DEVELOPMENT_STATUS,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Environment :: Web Environment',
        'Framework :: Django',
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
    ],
)

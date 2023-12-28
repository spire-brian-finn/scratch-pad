from setuptools import setup, find_packages
from os import environ

setup(
    name="the_package",
    version="0.0.0",
    zip_safe=False,
    packages=find_packages(),
    scripts=["bin/use_the_package", "bin/test_script.sh"],
    author="Brian Finn",
    author_email="brian.finn@spire.com",
    description="A test for packaging non-python scripts with setuptools",
    )
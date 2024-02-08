from setuptools import setup, find_packages
import pathlib

__version__ = "0.0.01"

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="BIO120",
    version=__version__,
    long_description=README,
    description="Laboratory class in advanced microbiology",
    long_description_content_type='text/markdown',
    url="https://github.com/BIO120/bio120",
    license="GPLv3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
    ],
    author="Sharon Long, Naima Sharaf, Jonas Cremer",
    author_email="jbcremer@stanford.edu",
    packages=find_packages(
        exclude=('docs', 'source', 'doc', 'sandbox', 'dev',)),
    include_package_data=True
)

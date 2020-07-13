# -*- coding: utf-8 -*-

import os
from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# load the package's __version__.py module as a dictionary
about = {}
with open(os.path.join(here, "profiler2", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

try:
    with open("README.md", "r") as f:
        readme = f.read()
except FileNotFoundError:
    readme = about["__description__"]

packages = ["profiler2"]

requires = ["scapy==2.4.3", "manuf==1.1.1", "pytest==5.4.3", "tox==3.15.2"]

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    python_requires="~=3.7,",
    license=about["__license__"],
    classifiers=[
        "Natural Language :: English",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: System Administrators",
        "Topic :: Utilities",
    ],
    packages=packages,
    project_urls={
        "Documentation": "https://docs.wlanpi.com",
        "Source": "https://github.com/joshschmelzle/profiler2",
    },
    include_package_data=True,
    install_requires=requires,
    entry_points={"console_scripts": ["profiler=profiler2.__main__:main"]},
)

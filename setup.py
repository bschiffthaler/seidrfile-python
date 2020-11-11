import os
import re
import sys
import platform
import subprocess

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils.version import LooseVersion

with open("README.md", "r") as fh:
    long_description = fh.read()

version = str(sys.version_info.major) + str(sys.version_info.minor)

setup(
    name="SeidrFile",
    version="0.1.0",
    author="Bastian Schiffthaler",
    author_email="b.schiffthaler@gmail.com",
    description="Python bindings for SeidrFiles",
    long_description=long_description,
    packages=find_packages(),
    ext_modules=[Extension(
        "libseidrfile",
        ["src/wrapper.cpp", "bgzf/bgzf.c", "src/Serialize.cpp"],
        include_dirs=["src", "bgzf"],
        library_dirs=["/usr/local/lib"],
        libraries=["boost_python{}".format(version), "z"],
        extra_compile_args=["-O3", "-std=c++11"],
    )],
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: POSIX :: Linux",
    ],
)

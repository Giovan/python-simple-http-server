# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_eureka_client",
    version="0.0.2",
    author="Keijack",
    author_email="keijack.wu@gmail.com",
    description="An eureka client written in python, you can easily intergrate your python components with spring cloud.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keijack/python-simple-http-server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="markdown-structure-splitter",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-docx",
        "langchain-text-splitters",
    ],
    python_requires=">=3.10",
    author="Han Wenbo",
    author_email="",
    description="A tool for splitting markdown files while preserving structure",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/markdown-structure-splitter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
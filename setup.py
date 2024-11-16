# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except:
    long_description = "A tool for splitting markdown files while preserving structure"

setup(
    name="markdown-hierarchy-splitter",
    # 使用标准版本格式
    version="0.1.0.dev0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-docx>=0.8.10",
        "langchain-text-splitters>=0.0.1",
        "setuptools>=61.0.0"  # 添加setuptools最低版本要求
    ],
    python_requires=">=3.10",
    author="Han Wenbo",
    author_email="",
    description="A tool for splitting markdown files while preserving structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hwb96/markdown-structure-splitter",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
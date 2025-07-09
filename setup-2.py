#!/usr/bin/env python3
"""
Setup script for PubMed Gender Analysis Tool
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pubmed-gender-analysis",
    version="1.0.0",
    author="Plastic Surgery Gender Analysis Research Team",
    author_email="research@example.com",
    description="Large-scale gender analysis tool for academic literature using PubMed data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/pubmed-gender-analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800"
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5"
        ]
    },
    entry_points={
        "console_scripts": [
            "pubmed-gender-analysis=src.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    project_urls={
        "Bug Reports": "https://github.com/your-username/pubmed-gender-analysis/issues",
        "Source": "https://github.com/your-username/pubmed-gender-analysis",
        "Documentation": "https://github.com/your-username/pubmed-gender-analysis/docs",
    },
)
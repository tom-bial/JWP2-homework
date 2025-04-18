from setuptools import setup, find_packages

setup(
    name="geompy",
    version="0.1.0",
    author="Tomek",
    description="Biblioteka do obliczania podstawowych fłasności figur geometrycznych",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26"
    ],
)
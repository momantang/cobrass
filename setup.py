from setuptools import setup, find_packages

setup(
    name="cobrass",
    version="0.0.1.20181111",
    description="cobrass finance",
    author="cobrass",
    url="http://www.cobrass.css",
    license="Apache License 2.0",
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    # scripts=["scripts/test.py"],
)

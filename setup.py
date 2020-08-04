from setuptools import setup, find_packages
import sys

assert sys.version_info > (3, 6, 0), "Only support Python 3.6 and above."

with open("VERSION") as f:
    version = f.read()

setup(
    name="env-wrappers",
    packages=[p for p in find_packages() if p != "tests"],
    version=version,
    install_requires=["ml-logger"],
    description="A clean collection of gym environment wrappers",
    author="Ge Yang<ge.ike.yang@gmail.com>",
    license="MIT",
)

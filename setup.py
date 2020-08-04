from setuptools import setup
import sys

assert sys.version_info > (3, 6, 0), "Only support Python 3.6 and above."

with open("VERSION") as f:
    version = f.read()

setup(
    name="env-wrappers",
    py_modules=["env_wrappers"],
    version=version,
    install_requires=["ml-logger"],
    description="A clean collection of gym environment wrappers",
    author="Ge Yang<ge.ike.yang@gmail.com>",
    license="MIT",
)

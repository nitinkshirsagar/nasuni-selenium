from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="nasuni-selenium",
    description="nasuni selenium UI ",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="null",
    url="https://github.com/nitinkshirsagar/nasuni-selenium",
    project_urls={
        "Issues": "https://github.com/nitinkshirsagar/nasuni-selenium/issues",
        "CI": "https://github.com/nitinkshirsagar/nasuni-selenium/actions",
        "Changelog": "https://github.com/nitinkshirsagar/nasuni-selenium/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["nasuni_selenium"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)

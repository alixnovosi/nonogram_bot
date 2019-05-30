from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "VERSION"), encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(author="Andrew Michaud",
      author_email="bots+nonogram@mail.andrewmichaud.com",

      entry_points={
          "console_scripts": ["nonogram_bot = nonogram_bot.__main__:main"]
      },

      install_requires=["botskeleton>=3.3.3", "nonogen"],

      license="BSD3",

      name="nonogram_bot",

      python_requires=">=3.6",

      packages=find_packages(),

      url="https://github.com/alixnovosi/nonogram_bot",

      version=VERSION)

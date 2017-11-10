from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "VERSION"), encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(author="Andrew Michaud",
      author_email="bots@mail.andrewmichaud.com",

      entry_points={
          "console_scripts": ["nonobot_bot = nonobot_bot.__main__:main"]
      },

      install_requires=["botskeleton>=1.1.0", "nonogen"],

      license="BSD3",

      name="nonobot_bot",

      python_requires=">=3.6",

      packages=find_packages(),

      # Project"s main homepage
      url="https://github.com/andrewmichaud/nono_bot",

      version=VERSION)

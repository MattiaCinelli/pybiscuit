"""Simple script to run snips of code"""
# Standard Libraries

# Third party libraries

# Local imports
from {{cookiecutter.package_name}}.logs import logging

if __name__ == "__main__":
    logger = logging.getLogger("Main")
    logger.info("Running Main.py")
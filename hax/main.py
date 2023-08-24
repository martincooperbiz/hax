"""The entry point to the application"""
from os.path import dirname, realpath
from sys import path

from app import App

# import the root of the package
module_path = dirname(realpath(__file__))
path.append(module_path)


if __name__ == "__main__":
  app = App()
  app.run()

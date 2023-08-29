"""Import the application package"""
from os.path import dirname, realpath
from sys import path

# import the root of the package
hax_path = f"{dirname(realpath(__file__))}/../hax"
path.append(hax_path)

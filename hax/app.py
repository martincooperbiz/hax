"""Module of the main application form"""
from os.path import abspath, dirname, isfile
from tkinter import Tk

from classes.enums import Windows
from frames.about_frame import AboutFrame
from frames.main_menu import MainMenu
from frames.menubar import MenuBar
from frames.setting_frame import SettingFrame
from frames.sqli_frame import SqliFrame
from frames.xss_frame import XssFrame
from yaml import safe_load


class App(Tk):
  """class represents the main application form"""
  def __init__(self):
    super().__init__()
    self.config: dict = {}
    self.load_config(f"{dirname(abspath(__file__))}/config.yml")
    self.main_menu = MainMenu(master=self)
    self.menubar = MenuBar(master=self)
    self.__init_components__()
    self.current_frame = None

  def __init_components__(self):
    self.title("HaX Cybersecurity tool")
    self.geometry(self.config["app"]["size"])  # set the size of the app to specific dimension
    self.resizable(False, False)

    self.menubar.init_items()
    self.configure(menu=self.menubar)

    self.main_menu.init_items(self.fill_frame)
    self.main_menu.grid(column=0, row=0, sticky="nsw")

  def fill_frame(self, event, window: Windows):
    # pylint: disable=unused-argument
    """Fill a window into the main frame when a button click"""
    if self.current_frame:
      self.current_frame.destroy()
      self.current_frame = None

    if window == Windows.XSS:
      self.current_frame = XssFrame(self)
    elif window == Windows.SQLI:
      self.current_frame = SqliFrame(self)
    elif window == Windows.SETTING:
      self.current_frame = SettingFrame(self)
    elif window == Windows.ABOUT:
      self.current_frame = AboutFrame(self)
    else:
      raise NotImplementedError(f"The frame '{window}' hasn't implemented yet")
    self.current_frame.grid(row=0, column=1, sticky="nsew")

  def run(self):
    """run the main application interface"""
    self.mainloop()

  def load_config(self, config_path: str = "config.yml"):
    """load the application configuration file (YAML format)"""
    if not isfile(config_path):
      raise FileNotFoundError(f"Config file not found in path: {config_path}")
    self.config = safe_load(open(config_path, encoding="UTF-8"))

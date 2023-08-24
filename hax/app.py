"""Module of the main application form"""
from os.path import abspath, dirname, isfile
from tkinter import Button, Label, PhotoImage, Tk

from attacks.sqli.sqli_form import SqliForm
from attacks.xss.xss_form import XssForm
from classes.enums import AttackType
from yaml import safe_load


class App:
  """class represents the main application form"""

  def __init__(self):
    self.load_config(f"{dirname(abspath(__file__))}/config.yml")
    self.form = Tk()
    self.__init_form()

  def __init_form(self):
    """initialize the form components"""
    self.form.title("HaX Cybersecurity tool")
    self.form.geometry(self.config["app"]["size"])  # set the size of the app to specific dimension
    self.form.resizable(0, 0)  # don't allow resizing in the x or y direction
    self.tkimage = PhotoImage(file=self.config["images"]["logo"])
    self.lbl_banner = Label(self.form, image=self.tkimage)
    self.btn_xss = Button(self.form, width=30, text="XSS Attack", command=lambda: self.__open_form(AttackType.XSS))
    self.btn_sqli = Button(self.form, width=30, text="SQLi Attack", command=lambda: self.__open_form(AttackType.SQLI))
    self.lbl_banner.grid(row=0, column=0, pady=5, padx=5, columnspan=2)
    self.btn_xss.grid(row=1, column=0)
    self.btn_sqli.grid(row=1, column=1)

  def __open_form(self, attack_type: AttackType):
    """Open an attack form on a button click"""
    if attack_type == AttackType.XSS:
      XssForm(self.form)
    elif attack_type == AttackType.SQLI:
      SqliForm(self.form)
    else:
      raise NotImplementedError(f"The attack '{attack_type}' hasn't implemented yet")

  def run(self):
    """run the main application interface"""
    self.form.mainloop()

  def load_config(self, config_path: str = "config.yml"):
    """load the application configuration file (YAML format)"""
    if not isfile(config_path):
      raise FileNotFoundError(f"Config file not found in path: {config_path}")
    self.config = safe_load(open(config_path, encoding="UTF-8"))

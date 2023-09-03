"""SQLI injection frame"""
# pylint: disable=R0801
from os.path import abspath, dirname
from tkinter import INSERT, Tk

from attacks.sqli.sqli_attack import SqliAttack
from classes.enums import AttackType, RequestType
from frames.attack_frame import AttackFrame


class SqliFrame(AttackFrame):
  """CrossSite attack frame"""

  def __init__(self, master: Tk):
    payloads_path = f"{dirname(abspath(__file__))}/../attacks/sqli/payloads.txt"
    super().__init__(master, "SQLI Injection attack", payloads_path)

  def __init_frame__(self):
    """Initialize frame components"""
    super().__init_frame__()

    self.add_label("URL (without GET params)").grid(row=0, column=0)
    self.input_url = self.add_entry(width=40)
    self.input_url.grid(row=0, column=1, columnspan=2, pady=(10, 0))

    self.add_label(text="Paramaters sep by comma\n(e.g. par1,par2)").grid(row=1, column=0)
    self.input_parameters = self.add_entry(width=40)
    self.input_parameters.grid(row=1, column=1, columnspan=2)

    self.add_label("Placeholder Text\n(replaced in payloads)").grid(row=2, column=0)
    self.input_placeholder_text = self.add_entry(width=40)
    self.input_placeholder_text.grid(row=2, column=1, columnspan=2)

    self.add_label("Request type").grid(row=3, column=0)
    (self.opt_request_type, self.value_request_type) = self.add_option("Request type", *(RequestType.get_names()))
    self.opt_request_type.grid(row=3, column=1, columnspan=2, sticky="w")

    self.add_button("Start Attack", self.init_attack).grid(row=4, column=0, columnspan=3)

    self.progbar_attacks = self.add_progressbar(500)
    self.progbar_attacks.grid(row=5, column=0, columnspan=3, pady=(10, 10))

    self.txt_log = self.add_log(7, 0, 2, 12)

  def set_default_input(self):
    """default value for the input"""
    super().set_default_input()
    self.input_url.insert(INSERT, "https://google.com")
    self.input_parameters.insert(INSERT, "name")
    self.value_request_type.set("POST")

  def init_attack(self):
    """prepare the request and start the attack"""
    url = self.input_url.get()
    request_type = RequestType[self.value_request_type.get()]
    parameters = self.input_parameters.get().split(",")
    placeholder_text = self.input_placeholder_text.get()
    self.attack = SqliAttack(url, request_type, parameters, AttackType.SQLI)
    self.start_attack(placeholder_text)

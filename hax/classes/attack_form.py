"""The base class for other attack forms"""
from os.path import abspath, dirname
from tkinter import END, Text, Tk, Toplevel, ttk

from classes.attack import Attack
from classes.attack_request import AttackRequest


class AttackForm(Toplevel):
  """base class for the attack forms"""

  attack_num = 0

  def __init__(self, master: Tk, payloads_path: str = ""):
    super().__init__(master=master)
    self.init_form()
    self.set_default_input()
    if payloads_path:
      self.payloads_path = payloads_path
    else:
      self.payloads_path = f"{dirname(abspath(__file__))}/payloads.txt"

  def init_form(self):
    """Initialize form components"""
    self.title("Attack Form")
    self.txt_log = Text(self, height=30, width=120)
    self.progbar_attacks = ttk.Progressbar(self, orient="horizontal", mode="determinate", length=800)

  def set_default_input(self):
    """default value for the input"""
    # configuring the log tags to colorize output
    self.txt_log.tag_config("SUCCESS", background="green")
    self.txt_log.tag_config("FAILED", background="red")

  def attack(self, attack: Attack, placeholder_text: str):
    """Start the attack"""
    self.txt_log.delete(1.0, END)  # clear text
    self.attack_num = 0
    self.payloads = self.load_payloads(placeholder_text, self.payloads_path)
    attack.start(self.payloads, self.add_result)

  def add_result(self, payload: str, attack_request: AttackRequest):
    """Add result to the log text component"""
    response_result = ""
    response_result += f"PAYLOAD: {payload}\n"
    response_result += f"REQUEST URL: {attack_request.response.request.url}\n"
    response_result += f"REQUEST HEADERS: {attack_request.response.request.headers}\n"
    response_result += f"REQUEST BODY: {attack_request.response.request.body}\n"
    if attack_request.is_success:
      response_result += "The attack has succeded\n\n"
    else:
      response_result += "The attack has failed\n\n"
    response_result += "-" * 100
    response_result += "\n" * 2
    self.txt_log.insert(END, response_result)
    row = (self.attack_num * 8) + 5
    # add tag using indices for the part of text to be highlighted
    self.txt_log.tag_add("SUCCESS" if attack_request.is_success else "FAILED", f"{row}.0", f"{row}.100")
    self.txt_log.see(END)
    self.progbar_attacks.step(99.9 * 1 / len(self.payloads))
    self.attack_num += 1

  def load_payloads(self, placeholder_text, file_path):
    """Load the attack payloads from a file"""
    with open(file_path, "r", encoding="UTF-8") as payloads_file:
      return [payload.strip("\n").replace("{{PLACEHOLDER}}", placeholder_text) for payload in payloads_file.readlines()]

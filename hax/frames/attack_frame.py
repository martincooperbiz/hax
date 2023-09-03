"""base class for all attacks"""
from os.path import abspath, dirname
from tkinter import END

from classes.attack import Attack
from frames.base_frame import BaseFrame


class AttackFrame(BaseFrame):
  """base class for the attack forms"""

  attack_num = 0

  def __init__(self, master, title: str, payloads_path: str = ""):
    super().__init__(master=master, title=title)
    self.attack = None
    if payloads_path:
      self.payloads_path = payloads_path
    else:
      self.payloads_path = f"{dirname(abspath(__file__))}/payloads.txt"

  def __init_frame__(self):
    """Initialize frame components"""
    super().__init_frame__()
    self.progbar_attacks = self.add_progressbar(500)
    self.txt_log = self.add_log(7, 0, 2, 12)

  def set_default_input(self):
    """default value for the input"""
    # configuring the log tags to colorize output
    super().set_default_input()
    self.txt_log.tag_config("SUCCESS", background="green")
    self.txt_log.tag_config("FAILED", background="red")

  def destroy(self) -> None:
    if self.attack:
      self.attack.stop_attack()
    super().destroy()

  def start_attack(self, placeholder_text: str):
    """Start the attack"""
    if not self.attack:
      return
    self.txt_log.delete(1.0, END)  # clear text
    self.attack_num = 0
    self.payloads: list = self.load_payloads(placeholder_text, self.payloads_path)
    self.attack.start(self.payloads, self.add_result)

  def add_result(self, payload: str, attack: Attack):
    """Add result to the log text component"""
    response_result = ""
    response_result += f"PAYLOAD: {payload}\n"
    response_result += f"REQUEST URL: {attack.response.request.url}\n"
    response_result += f"REQUEST HEADERS: {attack.response.request.headers}\n"
    response_result += f"REQUEST BODY: {attack.response.request.body}\n"
    if attack.is_success:
      response_result += "The attack has succeded\n"
    else:
      response_result += "The attack has failed\n"
    response_result += "-" * 50
    response_result += "\n" * 2
    self.txt_log.insert(END, response_result)
    row = (self.attack_num * 7) + 5
    # add tag using indices for the part of text to be highlighted
    self.txt_log.tag_add("SUCCESS" if attack.is_success else "FAILED", f"{row}.0", f"{row}.100")
    self.txt_log.see(END)
    self.progbar_attacks.step(99.9 * (1 / len(self.payloads)))
    self.attack_num += 1

  def load_payloads(self, placeholder_text, file_path) -> list:
    """Load the attack payloads from a file"""
    with open(file_path, "r", encoding="UTF-8") as payloads_file:
      return [payload.strip("\n").replace("{{PLACEHOLDER}}", placeholder_text) for payload in payloads_file.readlines()]

"""About frmae"""
from frames.base_frame import BaseFrame

ABOUT_TXT = """
HaX is an AI-powered Cybersecurity tool designed to detect website vulnerabilities.
Its cloud connection enhances capabilities for advanced analytics and modeling.

Crafted by TLabs, this tool is open-source, operating under the GPL-3.0 license.

For more details please visit:
"""
LINK = "https://haxsec.com"


class AboutFrame(BaseFrame):
  """About frame"""
  def __init__(self, master):
    super().__init__(master, "About HaX")

  def __init_frame__(self):
    super().__init_frame__()
    self.columnconfigure(0, weight=1)
    self.add_image(self.master.app_config["images"]["logo"], 0, 0, pady=(25, 0))
    self.add_label(ABOUT_TXT, justify="center", wraplength=550).grid(row=1, column=0)
    self.add_link(LINK, LINK, 2, 0)

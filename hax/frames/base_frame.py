"""Base class for sub windows in the application"""
from os.path import abspath, dirname
from tkinter import END, Button, Entry, Frame, Label, OptionMenu, Scrollbar, StringVar, Text, Tk, ttk
from webbrowser import open_new

from classes.attack_request import AttackRequest
from PIL import Image, ImageTk


class BaseFrame(Frame):
  """Frame for sub windows in the application"""
  def __init__(self, master: Tk, title: str):
    self.master = master
    super().__init__(master, bg=self.master.config["style"]["third_color"])
    self.master.columnconfigure(1, weight=1)
    self.master.rowconfigure(0, weight=1)
    self.master.title(title)
    self.__init_frame__()

  def __init_frame__(self):
    self.custom_style = ttk.Style()
    self.custom_style.theme_use('clam')
    self.custom_style.configure("progress.Horizontal.TProgressbar",
                                background=self.master.config["style"]["primary_color"],
                                troughcolor=self.master.config["style"]["secondary_color"],
                                darkcolor=self.master.config["style"]["primary_color"],
                                lightcolor=self.master.config["style"]["primary_color"],
                                bordercolor=self.master.config["style"]["secondary_color"])

  def __add_default__(self, widget_type, **parameters):
    """Add default parameters"""
    if widget_type in [Button] and "highlightbackground" not in parameters:
      parameters["highlightbackground"] = self.master.config["style"]["third_color"]
    if widget_type not in [OptionMenu, ttk.Progressbar]:
      if "fg" not in parameters:
        parameters["fg"] = self.master.config["style"]["secondary_color"]
      if "bg" not in parameters and widget_type not in [Entry]:
        parameters["bg"] = self.master.config["style"]["third_color"]

      if widget_type is not Label:
        if "highlightbackground" not in parameters:
          parameters["highlightbackground"] = self.master.config["style"]["border_color"]
        if "highlightcolor" not in parameters:
          parameters["highlightcolor"] = self.master.config["style"]["primary_color"]
        if "highlightthickness" not in parameters:
          parameters["highlightthickness"] = 1
    return parameters

  def add_widget(self, widget_type: type, **parameters):
    """Add widget to the frame in specific cell and parameters"""
    parameters = self.__add_default__(widget_type, **parameters)
    widget = widget_type(self, **parameters)
    return widget

  def add_image(self, path, row, col, padx=(0, 0), pady=(0, 0)):
    """Add image to the frame in a specific grid cell"""
    img = ImageTk.PhotoImage(Image.open(path))
    img_widget = self.add_widget(Label, image=img, justify="center")
    img_widget.grid(row=row, column=col, padx=padx, pady=pady)
    img_widget.image = img
    return img_widget

  def add_link(self, text, link, row, col):
    """Add text link to the frame in a specific grid cell"""
    lbl_link = self.add_widget(Label, fg=self.master.config["style"]["primary_color"],
                               text=text, justify="center", cursor="hand2")
    lbl_link.bind("<Button-1>", lambda e: open_new(link))
    lbl_link.grid(row=row, column=col)

  def add_label(self, text, **parameters):
    """"Add label to the frame in a specific grid cell"""
    lbl = self.add_widget(Label, text=text, **parameters)
    return lbl

  def add_entry(self, **parameters):
    """"Add entry to the frame in a specific grid cell"""
    if "relief" not in parameters:
      parameters["relief"] = "flat"
    entry = self.add_widget(Entry, **parameters)
    return entry

  def add_button(self, text, **parameters):
    """"Add button to the frame in a specific grid cell"""
    btn = self.add_widget(Button, text=text, **parameters)
    return btn

  def add_progressbar(self, length):
    """"Add progress bar to the frame in a specific grid cell"""
    progbar = self.add_widget(ttk.Progressbar, style="progress.Horizontal.TProgressbar", orient="horizontal", mode="determinate", length=length)

    return progbar

  def add_option(self, name, *value, **parameters):
    """"Add option menu to the frame in a specific grid cell"""
    variables = StringVar(self)
    variables.set(name)
    option = OptionMenu(self, variables, *value, **parameters)
    return (option, variables)

  def add_log(self, row, col, colspan, height):
    """"Add log output to the frame in a specific grid cell"""
    ver_scrollbar = Scrollbar(self, orient="vertical")
    txt_log = self.add_widget(Text, height=height, yscrollcommand=ver_scrollbar.set, relief="flat")
    ver_scrollbar.config(command=txt_log.yview)
    txt_log.grid(row=row, column=col, columnspan=colspan, padx=(10, 0))
    ver_scrollbar.grid(row=row, column=col+colspan, sticky="nsw")
    return txt_log


class AttackFrame(BaseFrame):
  """base class for the attack forms"""

  attack_num = 0

  def __init__(self, master: Tk, title: str, payloads_path: str = ""):
    super().__init__(master=master, title=title)
    self.set_default_input()
    self.attack = None
    if payloads_path:
      self.payloads_path = payloads_path
    else:
      self.payloads_path = f"{dirname(abspath(__file__))}/payloads.txt"

  def __init_frame__(self):
    """Initialize frame components"""
    super().__init_frame__()
    self.txt_log = Text(self)
    self.progbar_attacks = ttk.Progressbar(self, orient="horizontal", mode="determinate", length=800)

  def set_default_input(self):
    """default value for the input"""
    # configuring the log tags to colorize output
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
    self.payloads = self.load_payloads(placeholder_text, self.payloads_path)
    self.attack.start(self.payloads, self.add_result)

  def add_result(self, payload: str, attack_request: AttackRequest):
    """Add result to the log text component"""
    response_result = ""
    response_result += f"PAYLOAD: {payload}\n"
    response_result += f"REQUEST URL: {attack_request.response.request.url}\n"
    response_result += f"REQUEST HEADERS: {attack_request.response.request.headers}\n"
    response_result += f"REQUEST BODY: {attack_request.response.request.body}\n"
    if attack_request.is_success:
      response_result += "The attack has succeded\n"
    else:
      response_result += "The attack has failed\n"
    response_result += "-" * 50
    response_result += "\n" * 2
    self.txt_log.insert(END, response_result)
    row = (self.attack_num * 7) + 5
    # add tag using indices for the part of text to be highlighted
    self.txt_log.tag_add("SUCCESS" if attack_request.is_success else "FAILED", f"{row}.0", f"{row}.100")
    self.txt_log.see(END)
    self.progbar_attacks.step(99.9 * 1 / len(self.payloads))
    self.attack_num += 1

  def load_payloads(self, placeholder_text, file_path):
    """Load the attack payloads from a file"""
    with open(file_path, "r", encoding="UTF-8") as payloads_file:
      return [payload.strip("\n").replace("{{PLACEHOLDER}}", placeholder_text) for payload in payloads_file.readlines()]

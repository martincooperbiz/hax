"""Base class for sub windows in the application"""
from tkinter import Button, Entry, Frame, Label, OptionMenu, Scrollbar, StringVar, Text, ttk
from webbrowser import open_new

from PIL import Image, ImageTk


class BaseFrame(Frame):
  """Frame for sub windows in the application"""
  def __init__(self, master, title: str):
    self.master = master
    super().__init__(master, bg=self.master.app_config["style"]["third_color"])  # type: ignore[attr-defined]
    self.master.columnconfigure(1, weight=1)
    self.master.rowconfigure(0, weight=1)
    self.master.title(title)  # type: ignore[attr-defined]
    self.__init_frame__()
    self.set_default_input()

  def __init_frame__(self):
    self.custom_style = ttk.Style()
    self.custom_style.theme_use('clam')
    self.custom_style.configure("progress.Horizontal.TProgressbar",
                                background=self.master.app_config["style"]["primary_color"],
                                troughcolor=self.master.app_config["style"]["secondary_color"],
                                darkcolor=self.master.app_config["style"]["primary_color"],
                                lightcolor=self.master.app_config["style"]["primary_color"],
                                bordercolor=self.master.app_config["style"]["secondary_color"])

  def __add_default__(self, widget_type, **parameters):
    """Add default parameters"""
    if widget_type in [Button] and "highlightbackground" not in parameters:
      parameters["highlightbackground"] = self.master.app_config["style"]["third_color"]
    if widget_type not in [ttk.Progressbar]:
      if "fg" not in parameters:
        parameters["fg"] = self.master.app_config["style"]["secondary_color"]
      if "bg" not in parameters and widget_type not in [Entry]:
        parameters["bg"] = self.master.app_config["style"]["third_color"]
      elif widget_type is Entry:
        parameters["background"] = self.master.app_config["style"]["forth_color"]

      if widget_type is not Label:
        if "highlightbackground" not in parameters:
          parameters["highlightbackground"] = self.master.app_config["style"]["border_color"]
        if "highlightcolor" not in parameters:
          parameters["highlightcolor"] = self.master.app_config["style"]["primary_color"]
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
    lbl_link = self.add_widget(Label, fg=self.master.app_config["style"]["primary_color"],
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

  def add_button(self, text, click_func, **parameters):
    """"Add button to the frame in a specific grid cell"""
    if "command" not in parameters:
      parameters["command"] = click_func
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
    self.__add_default__(OptionMenu, **parameters)
    option = OptionMenu(self, variables, *value, **parameters)
    option.config(bg=self.master.app_config["style"]["third_color"],
                  fg=self.master.app_config["style"]["secondary_color"])
    return (option, variables)

  def add_log(self, row, col, colspan, height):
    """"Add log output to the frame in a specific grid cell"""
    ver_scrollbar = Scrollbar(self, orient="vertical")
    txt_log = self.add_widget(Text, height=height, yscrollcommand=ver_scrollbar.set, relief="flat")
    ver_scrollbar.config(command=txt_log.yview)
    txt_log.grid(row=row, column=col, columnspan=colspan, padx=(10, 0))
    ver_scrollbar.grid(row=row, column=col+colspan, sticky="nsw")
    return txt_log

  def set_default_input(self):
    """default value for the input"""

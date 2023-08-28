"""Module of the main application form"""
from os.path import abspath, dirname, isfile
from tkinter import Frame, Label, Menu, Tk

from classes.enums import AttackType, Windows
from frames.about_frame import AboutFrame
from frames.setting_frame import SettingFrame
from frames.sqli_frame import SqliFrame
from frames.xss_frame import XssFrame
from PIL import Image, ImageTk
from yaml import safe_load


class App:
  """class represents the main application form"""

  class MenuItem:
    """Class represent one menu item in the app"""
    def __init__(self, name, image, event):
      self.name = name
      self.image = image
      self.event = event

  def __init__(self):
    self.load_config(f"{dirname(abspath(__file__))}/config.yml")
    self.form = Tk()
    self.__init_form()

  def __init_form(self):
    """initialize the form components"""
    self.form.title("HaX Cybersecurity tool")
    self.form.geometry(self.config["app"]["size"])  # set the size of the app to specific dimension
    self.form.resizable(False, False)

    self.__init_menubar__()
    self.__init_main_menu__()

  def __init_menubar__(self):
    self.menubar = Menu(self.form)
    filemenu = Menu(self.menubar, tearoff=0)
    filemenu.add_command(label="New", command={})
    filemenu.add_command(label="Open", command={})
    filemenu.add_command(label="Save", command={})
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=self.form.quit)
    self.menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(self.menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command={})
    helpmenu.add_command(label="About...", command={})
    self.menubar.add_cascade(label="Help", menu=helpmenu)

    self.form.configure(menu=self.menubar)

  def __init_main_menu__(self):
    self.lst_menu = [
      App.MenuItem("XSS Attack", "xss.png", lambda event: self.__fill_frame__(event, Windows.XSS)),
      App.MenuItem("SQLi Attack", "sqli.png", lambda event: self.__fill_frame__(event, Windows.SQLI)),
      App.MenuItem("", "", lambda event: self.__fill_frame__(event, AttackType.XSS)),
      App.MenuItem("", "", lambda event: self.__fill_frame__(event, AttackType.XSS)),
      App.MenuItem("", "", lambda event: self.__fill_frame__(event, AttackType.XSS)),
      App.MenuItem("Setting", "setting.png", lambda event: self.__fill_frame__(event, Windows.SETTING)),
      App.MenuItem("About HaX", "about.png", lambda event: self.__fill_frame__(event, Windows.ABOUT))
    ]

    self.main_menu = Frame(self.form, bg="black")
    self.main_menu.grid(column=0, row=0)
    for item in self.lst_menu:
      btn_frame = Frame(self.main_menu, bg="black")
      btn_frame.grid(column=0)
      self.create_lbl_image(btn_frame, f"{' '*5}{item.name}", item.image, item.event).grid()

  def create_lbl_image(self, parent, text, image, event):
    """Create Button label"""
    img = ImageTk.PhotoImage((Image.open(f"static/images/{image}")).resize((30, 30))) if image else None

    if img:
      btn_lbl = Label(parent, width=200, height=50, text=text, image=img, compound='left',
                      background="#000", foreground="#fff", anchor="w", cursor="hand2")
      btn_lbl.image = img
      btn_lbl.bind("<Button-1>", event)

      def mouse_hover(event):
        # pylint: disable=unused-argument
        btn_lbl["background"] = "#222"

      def mouse_leave(event):
        # pylint: disable=unused-argument
        btn_lbl["background"] = "#000"

      btn_lbl.bind("<Enter>", mouse_hover)
      btn_lbl.bind("<Leave>", mouse_leave)
    else:
      btn_lbl = Label(parent, height=3, text=text, background="#000")
    return btn_lbl

  def __fill_frame__(self, event, frame: Windows):
    # pylint: disable=unused-argument
    """Open an attack form on a button click"""
    if frame == Windows.XSS:
      XssFrame(self.form)
    elif frame == Windows.SQLI:
      SqliFrame(self.form)
    elif frame == Windows.SETTING:
      SettingFrame(self.form)
    elif frame == Windows.ABOUT:
      AboutFrame(self.form)
    else:
      raise NotImplementedError(f"The attack '{frame}' hasn't implemented yet")

  def run(self):
    """run the main application interface"""
    self.form.mainloop()

  def load_config(self, config_path: str = "config.yml"):
    """load the application configuration file (YAML format)"""
    if not isfile(config_path):
      raise FileNotFoundError(f"Config file not found in path: {config_path}")
    self.config = safe_load(open(config_path, encoding="UTF-8"))

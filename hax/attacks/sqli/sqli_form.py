from tkinter import Tk, Entry, Button, Text, StringVar, OptionMenu, Label, \
                    Scrollbar, ttk, INSERT, W, N, S
from classes.attack_request import AttackRequest, RequestType, AttackType
from classes.attack import Attack
from classes.attack_form import AttackForm
from os.path import abspath, dirname


class SqliForm(AttackForm):
  def __init__(self, master: Tk):
    payloads_path = f"{dirname(abspath(__file__))}/payloads.txt"
    super().__init__(master, payloads_path)

  def init_form(self):
    self.title("SQL injection attack")

    self.lbl_url = Label(self, text="URL (without GET params)")
    self.input_url = Entry(self, width=70)

    self.lbl_parameters = Label(self, text="Paramaters sep by comma\n(e.g. par1,par2)")
    self.input_parameters = Entry(self, width=24)

    self.lbl_placeholder_text = Label(self, text="Placeholder Text\n(replaced in payloads)")
    self.input_placeholder_text = Entry(self, width=24)

    self.lbl_request_type = Label(self, text="Request type")
    self.value_request_type = StringVar(self)
    self.value_request_type.set("Request type")
    self.opt_request_type = OptionMenu(self, self.value_request_type,
                                       *(RequestType._member_names_))

    self.btn_start = Button(self, width=30, text="Start Attack", command=self.init_attack)
    self.progbar_attacks = ttk.Progressbar(self, orient='horizontal', mode='determinate', length=800)

    self.ver_scrollbar = Scrollbar(self, orient='vertical')
    self.lbl_log = Label(self, text="Output")
    self.txt_log = Text(self, height=30, width=120, yscrollcommand=self.ver_scrollbar.set)
    self.ver_scrollbar.config(command=self.txt_log.yview)

    self.lbl_url.grid(row=0, column=0, pady=2, padx=5, sticky=W)
    self.input_url.grid(row=0, column=1, pady=2, padx=5, sticky=W, columnspan=4)

    self.lbl_parameters.grid(row=1, column=0, pady=2, padx=5, sticky=W)
    self.input_parameters.grid(row=1, column=1, pady=2, sticky=W, padx=5)

    self.lbl_placeholder_text.grid(row=1, column=2, pady=2, padx=5, sticky=W)
    self.input_placeholder_text.grid(row=1, column=3, pady=2, padx=5, sticky=W)

    self.lbl_request_type.grid(row=2, column=0, pady=2, padx=5, sticky=W)
    self.opt_request_type.grid(row=2, column=1, pady=2, padx=5, sticky=W)

    self.btn_start.grid(row=3, column=0, pady=2, padx=5, columnspan=4)
    self.progbar_attacks.grid(row=4, column=0, pady=2, padx=5, columnspan=4)

    self.lbl_log.grid(row=5, column=0, pady=2, padx=5, sticky=W, columnspan=4)
    self.txt_log.grid(row=6, column=0, pady=2, padx=5, columnspan=4)
    self.ver_scrollbar.grid(row=6, column=4, sticky=N+S+W)

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
    request = AttackRequest(url, request_type, parameters, AttackType.SQLi)
    attack = Attack(request)
    self.attack(attack, placeholder_text)

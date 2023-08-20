from tkinter import Tk, Entry, Button, Text, StringVar, OptionMenu, Label, \
                    Scrollbar, ttk, INSERT, END, W, N, S
from attack_request import AttackRequest, RequestType, AttackType
from attack import Attack


class XssForm:
  form = Tk()

  def __init__(self):
    self.init_form()
    self.set_default_input()

  def init_form(self):
    self.form.title("Ethical Hacking - XSS")

    self.lbl_banner = Label(self.form, text="Cross Site scripting Attack")

    self.lbl_url = Label(self.form, text="URL (without GET params)")
    self.input_url = Entry(self.form, width=70)

    self.lbl_parameters = Label(self.form, text="Paramaters sep by comma\n(e.g. par1,par2)")
    self.input_parameters = Entry(self.form, width=24)

    self.lbl_placeholder_text = Label(self.form, text="Placeholder Text\n(replaced in payloads)")
    self.input_placeholder_text = Entry(self.form, width=24)

    self.lbl_request_type = Label(self.form, text="Request type")
    self.value_request_type = StringVar(self.form)
    self.value_request_type.set("Request type")
    self.opt_request_type = OptionMenu(self.form, self.value_request_type,
                                       *(RequestType._member_names_))

    self.btn_start = Button(self.form, width=30, text="Start Attack", command=self.attack)
    self.progbar_attacks = ttk.Progressbar(self.form, orient='horizontal', mode='determinate', length=800)

    self.ver_scrollbar = Scrollbar(self.form, orient='vertical')
    self.lbl_log = Label(self.form, text="Output")
    self.txt_log = Text(self.form, height=30, width=120, yscrollcommand=self.ver_scrollbar.set)
    self.ver_scrollbar.config(command=self.txt_log.yview)

    self.lbl_banner.grid(row=0, column=0, columnspan=4)

    self.lbl_url.grid(row=1, column=0, pady=2, padx=5, sticky=W)
    self.input_url.grid(row=1, column=1, pady=2, padx=5, sticky=W, columnspan=4)

    self.lbl_parameters.grid(row=2, column=0, pady=2, padx=5, sticky=W)
    self.input_parameters.grid(row=2, column=1, pady=2, sticky=W, padx=5)

    self.lbl_placeholder_text.grid(row=2, column=2, pady=2, padx=5, sticky=W)
    self.input_placeholder_text.grid(row=2, column=3, pady=2, padx=5, sticky=W)

    self.lbl_request_type.grid(row=3, column=0, pady=2, padx=5, sticky=W)
    self.opt_request_type.grid(row=3, column=1, pady=2, padx=5, sticky=W)

    self.btn_start.grid(row=4, column=0, pady=2, padx=5, columnspan=4)
    self.progbar_attacks.grid(row=5, column=0, pady=2, padx=5, columnspan=4)

    self.lbl_log.grid(row=6, column=0, pady=2, padx=5, sticky=W, columnspan=4)
    self.txt_log.grid(row=7, column=0, pady=2, padx=5, columnspan=4)
    self.ver_scrollbar.grid(row=7, column=4, sticky=N+S+W)

  def set_default_input(self):
    """default value for the input"""
    self.input_url.insert(INSERT, "https://google.com")
    self.input_parameters.insert(INSERT, "name")
    self.value_request_type.set("POST")

    # configuring the log tags to colorize output
    self.txt_log.tag_config("SUCCESS", background="green")
    self.txt_log.tag_config("FAILED", background="red")

  def attack(self):
    """prepare the request and start the attack"""
    url = self.input_url.get()
    request_type = RequestType[self.value_request_type.get()]
    parameters = self.input_parameters.get().split(",")
    placeholder_text = self.input_placeholder_text.get()
    request = AttackRequest(url, request_type, parameters, AttackType.XSS)

    self.txt_log.delete(1.0, END)  # clear text
    self.ATTACK_NUM = 0
    attack = Attack(request)
    self.payloads = self.load_payloads(placeholder_text, "app/attacks/xss/xss_payloads.txt")
    attack.start(self.payloads, self.add_result)

  def add_result(self, result, is_success):
    self.txt_log.insert(END, result)
    row = (self.ATTACK_NUM*8)+5
    # add tag using indices for the part of text to be highlighted
    self.txt_log.tag_add("SUCCESS" if is_success else "FAILED", f"{row}.0", f"{row}.100")
    self.txt_log.see(END)
    self.progbar_attacks.step(99.9 * 1/len(self.payloads))
    self.ATTACK_NUM += 1

  def load_payloads(self, placeholder_text, file_path):
    with open(file_path, "r") as payloads_file:
      return [payload.strip("\n").replace("{{PLACEHOLDER}}", placeholder_text) for payload in payloads_file.readlines()]

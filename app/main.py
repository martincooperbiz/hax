from attacks.xss.xss_form import XssForm


def run_xss_form():
  xss_form = XssForm()
  xss_form.form.mainloop()


if __name__ == "__main__":
  run_xss_form()

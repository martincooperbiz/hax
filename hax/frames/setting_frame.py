"""Setting frame"""
from frames.base_frame import BaseFrame


class SettingFrame(BaseFrame):
  """Setting frame"""
  def __init__(self, master):
    super().__init__(master, "Setting")

  def __init_frame__(self):
    super().__init_frame__()
    self.columnconfigure(1, weight=1)

    self.add_label("AWS access key ID").grid(row=0, column=0)
    self.aws_access_key_id = self.add_entry(width=40)
    self.aws_access_key_id.grid(row=0, column=1, pady=(10, 5))

    self.add_label("AWS secret access key").grid(row=1, column=0)
    self.aws_secret_access_key = self.add_entry(width=40)
    self.aws_secret_access_key.grid(row=1, column=1)

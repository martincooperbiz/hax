"""Database exceptions"""


class SQLException(Exception):
  """raise when sql command failes"""
  def __init__(self, command, args=None):
    super().__init__(args)
    self.command = command

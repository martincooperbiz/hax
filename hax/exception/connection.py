"""Exceptions related to connection with endpoint"""


class ConnectionFailedException(Exception):
  """Exception raise when the connection with server fails"""
  def __init__(self, server, reason, *args, **kwargs):
    super().__init__(args, kwargs)
    self.server = server
    self.reason = reason

  def __str__(self) -> str:
    return f"Failed connecting to server {self.server}, reason: {self.reason}, more details {super().__str__()}"

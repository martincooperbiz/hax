"""Attack request module"""
from classes.enums import AttackType, RequestType
from requests import Response


class AttackRequest:
  """Class represent attack details to send it to the server"""
  # pylint: disable=too-few-public-methods

  def __init__(self, url: str, request_type: RequestType, paramaters: list, attack_type: AttackType):
    self.request_type = request_type
    self.url = url
    self.paramaters = paramaters
    self.attack_type = attack_type
    self.response = Response()
    self.is_success = False

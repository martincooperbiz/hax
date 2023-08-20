from enum import Enum


class RequestType(Enum):
  POST = 1
  GET = 2


class AttackType(Enum):
  XSS = 1
  SQLi = 2


class AttackRequest:
  def __init__(self, url: str, request_type: RequestType, paramaters: list, attack_type: AttackType):
    self.request_type = request_type
    self.url = url
    self.paramaters = paramaters
    self.attack_type = attack_type

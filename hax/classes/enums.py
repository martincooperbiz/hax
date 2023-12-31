"""All enums in the app"""
from enum import Enum


class RequestType(Enum):
  """All request types"""
  POST = 1
  GET = 2

  @classmethod
  def get_names(cls):
    """Get all enum names"""
    # pylint: disable=W0212,E1101
    return RequestType._member_names_


class AttackType(Enum):
  """All attack types"""
  XSS = 1
  SQLI = 2


class Windows(Enum):
  """All frames available"""
  NONE = 0
  XSS = 1
  SQLI = 2
  SETTING = 20
  ABOUT = 30


class Table(Enum):
  """All tables in the database"""
  SETTING = 1
  ATTACK = 2

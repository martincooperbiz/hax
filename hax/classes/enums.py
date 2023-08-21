from enum import Enum


class RequestType(Enum):
  POST = 1
  GET = 2


class AttackType(Enum):
  XSS = 1
  SQLi = 2

"""Module providing CrossSite Scripting injection attack"""
from re import IGNORECASE, search

from classes.attack import Attack

XSS_SUCCESS_PATTEREN = r"<script[^\n]*>[^\n]*(`|\(\"|\(\')xss(`|\"\)|'\))[^\n]*<\/script[^\n]*>"


class XssAttack(Attack):
  """Class represent a CrossSite attack"""

  def is_attack_succeeded(self):
    """Examine the response content to identify whether the CrossSite Scripting attack was successful"""
    response_body = self.response.content.decode()
    return search(pattern=XSS_SUCCESS_PATTEREN, string=response_body, flags=IGNORECASE)

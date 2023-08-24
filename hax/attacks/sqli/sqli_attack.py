"""Module providing SQLI injection attack"""
from classes.attack import Attack


class SqliAttack(Attack):
  """Class represent a normal SQL injection attack"""

  def is_attack_succeeded(self):
    """Examine the response status code to identify whether the SQL injection attack was successful"""
    if self.attack_request.response.status_code == 200:
      return True
    else:
      return False
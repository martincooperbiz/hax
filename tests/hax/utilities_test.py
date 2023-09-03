"""Test class for Utilities methods"""


from classes.attack import Attack
from classes.enums import AttackType, RequestType
from exceptions.connection import ConnectionFailedException
from pytest import raises


def test_send_http_request_valid_url():
  """Test the send_http_request method with valid URL"""
  attack = Attack("https://google.com", RequestType.GET, "", AttackType.XSS)
  resp = attack.send_http_request("")
  assert resp.status_code == 200

def test_send_http_request_invalid_url():
  """Test the send_http_request method with invalid URL"""
  with raises(ConnectionFailedException):
    attack = Attack("https://notexisturl.com", RequestType.GET, "", AttackType.XSS)
    attack.send_http_request("")

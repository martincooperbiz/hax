"""Test class for Utilities methods"""


from classes.attack_request import AttackRequest
from classes.enums import AttackType, RequestType
from exception.connection import ConnectionFailedException
from pytest import raises
from utilities.http_request import send_http_request


def test_send_http_request_valid_url():
  """Test the send_http_request method with valid URL"""
  att_req = AttackRequest("https://google.com", RequestType.GET, "", AttackType.XSS)
  resp = send_http_request(att_req, "")
  assert resp.status_code == 200

def test_send_http_request_invalid_url():
  """Test the send_http_request method with invalid URL"""
  with raises(ConnectionFailedException):
    att_req = AttackRequest("https://notexisturl.com", RequestType.GET, "", AttackType.XSS)
    send_http_request(att_req, "")

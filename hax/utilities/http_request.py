"""HTTP Request wrapper module"""
import requests
from classes.attack_request import AttackRequest, RequestType
from exception.connection import ConnectionFailedException


def send_http_request(attack_request: AttackRequest, attack_payload: str) -> requests.Response:
  """initialize HTTP request and return response"""
  headers = {"User-Agent": "Mozilla/5.0"}
  try:
    if attack_request.request_type == RequestType.POST:
      payload = {parameter: attack_payload for parameter in attack_request.paramaters}
      response = requests.post(url=attack_request.url, headers=headers, data=payload, timeout=30)
    elif attack_request.request_type == RequestType.GET:
      form_data = []
      for parameter in attack_request.paramaters:
        form_data.append(f"{parameter}={attack_payload}")
      request_url = f"{attack_request.url.split('?', 1)[0]}?{'&'.join(form_data)}"
      response = requests.get(url=request_url, headers=headers, timeout=30)
    return response
  except requests.exceptions.ConnectTimeout as ex:
    raise ConnectionFailedException(attack_request.url, "Timeout", ex.args) from ex
  except requests.exceptions.ConnectionError as ex:
    raise ConnectionFailedException(attack_request.url, "Connection Error", ex.args) from ex
  except Exception as ex:
    raise ConnectionFailedException(attack_request, "Unkown", ex.args) from ex

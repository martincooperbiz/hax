"""HTTP Request wrapper module"""
from classes.attack_request import AttackRequest, RequestType
from requests import Response, get, post


def send_http_request(attack_request: AttackRequest, attack_payload: str) -> Response:
  """initialize HTTP request and return response"""
  headers = {"User-Agent": "Mozilla/5.0"}
  if attack_request.request_type == RequestType.POST:
    payload = {parameter: attack_payload for parameter in attack_request.paramaters}
    response = post(url=attack_request.url, headers=headers, data=payload, timeout=30)
  elif attack_request.request_type == RequestType.GET:
    form_data = []
    for parameter in attack_request.paramaters:
      form_data.append(f"{parameter}={attack_payload}")
    request_url = f"{attack_request.url.split('?', 1)[0]}?{'&'.join(form_data)}"
    response = get(url=request_url, headers=headers, timeout=30)
  return response

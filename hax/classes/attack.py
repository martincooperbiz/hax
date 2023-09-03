"""Attack Module"""
from threading import Thread
from time import sleep

import requests
from classes.enums import AttackType, RequestType
from exceptions.connection import ConnectionFailedException
from requests import Response


class Attack:
  """Class represents Cyber Attack"""
  payloads: list = []

  def __init__(self, url: str, request_type: RequestType, paramaters: list, attack_type: AttackType):
    self.request_type = request_type
    self.url = url
    self.paramaters = paramaters
    self.attack_type = attack_type
    self.response = Response()
    self.is_success = False

  def start(self, payloads, add_result_func):
    """Start the attack in separate thread"""
    self.attack_thread = Thread(
        target=self.start_attack,
        args=(
            payloads,
            add_result_func,
        ),
    )
    self.attack_thread.start()

  def start_attack(self, payloads, add_result_func):
    """Initiate the attack using all provided payloads"""
    self.stop_flag = False
    for payload in payloads:
      # for each payload, get the request ready and then send it to the server
      with self.send_http_request(payload) as response:
        # get the attack result
        self.response = response
        self.is_success = self.is_attack_succeeded()
        if self.stop_flag:
          return
        add_result_func(payload, self)
        sleep(0.1)

  def stop_attack(self):
    """Stop the attack"""
    self.stop_flag = True

  def is_attack_succeeded(self):
    """Examine the response to identify whether the attack was successful"""
    return self.response.status_code == 200

  def send_http_request(self, attack_payload: str) -> requests.Response:
    """initialize HTTP request and return response"""
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
      if self.request_type == RequestType.POST:
        payload = {parameter: attack_payload for parameter in self.paramaters}
        response = requests.post(url=self.url, headers=headers, data=payload, timeout=30)
      elif self.request_type == RequestType.GET:
        form_data = []
        for parameter in self.paramaters:
          form_data.append(f"{parameter}={attack_payload}")
        request_url = f"{self.url.split('?', 1)[0]}?{'&'.join(form_data)}"
        response = requests.get(url=request_url, headers=headers, timeout=30)
      return response
    except requests.exceptions.ConnectTimeout as ex:
      raise ConnectionFailedException(self.url, "Timeout", ex.args) from ex
    except requests.exceptions.ConnectionError as ex:
      raise ConnectionFailedException(self.url, "Connection Error", ex.args) from ex
    except Exception as ex:
      raise ConnectionFailedException(self, "Unkown", ex.args) from ex

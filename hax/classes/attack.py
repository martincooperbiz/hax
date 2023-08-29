"""Attack Module"""
from threading import Thread
from time import sleep

from classes.attack_request import AttackRequest
from utilities.http_request import send_http_request


class Attack:
  """Class represents Cyber Attack"""
  payloads: list = []

  def __init__(self, attack_request: AttackRequest):
    self.attack_request = attack_request

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
      with send_http_request(self.attack_request, payload) as response:
        # get the attack result
        self.attack_request.response = response
        self.attack_request.is_success = self.is_attack_succeeded()
        if self.stop_flag:
          return
        add_result_func(payload, self.attack_request)
        sleep(0.1)

  def stop_attack(self):
    """Stop the attack"""
    self.stop_flag = True

  def is_attack_succeeded(self):
    """Examine the response to identify whether the attack was successful"""
    return self.attack_request.response.status_code == 200

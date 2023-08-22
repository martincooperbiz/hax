from classes.attack_request import AttackRequest
from utilities.http_request import send_http_request
from threading import Thread
from time import sleep


class Attack:
  payloads = []

  def __init__(self, attack_request: AttackRequest):
    self.attack_request = attack_request

  def start(self, payloads, add_result_func):
    attack_thread = Thread(target=self.start_attack, args=(payloads, add_result_func,))
    attack_thread.start()

  def start_attack(self, payloads, analyse_result_func):
    for payload in payloads:
      with send_http_request(self.attack_request, payload) as response:
        analyse_result_func(payload, response)
        sleep(0.1)

from attack_request import AttackRequest
from utilities import send_http_request
import re
from threading import Thread
from time import sleep

XSS_SUCCESS_PATTEREN = r"<script[^\n]*>[^\n]*(`|\(\"|\(\')xss(`|\"\)|'\))[^\n]*<\/script[^\n]*>"


class Attack:
  payloads = []

  def __init__(self, attack_request: AttackRequest):
    self.attack_request = attack_request

  def start(self, payloads, add_result_func):
    attack_thread = Thread(target=self.start_attack, args=(payloads, add_result_func,))
    attack_thread.start()

  def start_attack(self, payloads, add_result_func):
    for payload in payloads:
      response_result = ""
      with send_http_request(self.attack_request, payload) as response:
        response_body = response.content.decode()
        response_result += f"PAYLOAD: {payload}\n"
        response_result += f"REQUEST URL: {response.request.url}\n"
        response_result += f"REQUEST HEADERS: {response.request.headers}\n"
        response_result += f"REQUEST BODY: {response.request.body}\n"
        is_success = re.search(pattern=XSS_SUCCESS_PATTEREN, string=response_body, flags=re.IGNORECASE)
        if is_success:
          response_result += "The attack has succeded\n\n"
        else:
          response_result += "The attack has failed\n\n"
        response_result += "-" * 100
        response_result += "\n" * 2

        add_result_func(response_result, is_success)
        sleep(0.1)

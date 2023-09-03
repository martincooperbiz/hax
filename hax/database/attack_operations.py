"""Database operation related to the attacks"""
from classes.attack import Attack
from classes.enums import AttackType, RequestType, Table
from database.db import DB
from database.table_operations import run, select_all, select_item

db = DB()


def add_attack(attack: Attack):
  """Insert attack into database"""
  command = "INSERT INTO attack (url, parameters) values (?, ?)"
  args = (attack.url, attack.paramaters)
  return run(command, args)


def insert_attack(url: str, request_type: RequestType, attack_type: AttackType, parameters: str):
  """insert setting into database"""
  command = "INSERT INTO setting (url, request_type, parameters, attack_type) values (?, ?, ?, ?)"
  args = (url, request_type, parameters, attack_type,)
  return run(command, args)


def update_attack(item_id: int, url: str, request_type: RequestType, attack_type: AttackType, parameters: str):
  """update attack in the database"""
  command = """UPDATE attack SET
    url = ?,
    request_type = ?
    parameters = ?
    attack_type = ?
  WHERE id = ?"""
  args = (url, request_type, parameters, attack_type, item_id,)
  return run(command, args)


def get_attack_by_url(url: str):
  """get attack from database using its url"""
  return select_item(Table.ATTACK, [("url", url)])


def get_all_attacks():
  """get all attacks from database"""
  result = select_all(Table.ATTACK)
  attacks = []
  for item in result:
    request_type = RequestType(item[2])
    attack_type = AttackType(item[4])
    attacks.append(Attack(item[1], request_type, item[3], attack_type))
  return attacks

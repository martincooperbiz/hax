"""Database operation related to the setting"""
from classes.enums import Table
from database.table_operations import run, select_all, select_item


def update_setting(name: str, value: str):
  """insert setting into database"""
  item = get_setting_by_name(name)
  args: tuple = tuple()
  if item:
    command = "UPDATE setting SET name = ?, value = ? WHERE id = ?"
    item_id = item[0]
    args = (name, value, item_id)
  else:
    command = "INSERT INTO setting (name, value) values (?, ?)"
    args = (name, value)
  return run(command, args)


def get_setting_by_name(name: str):
  """get setting value from database"""
  return select_item(Table.SETTING, [("name", name)])


def get_all_setting():
  """get setting value from database"""
  result = select_all(Table.SETTING)
  setting = {}
  for item in result:
    setting[item[1]] = item[2]
  return setting

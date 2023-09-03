"""Database operation related to the setting"""
from classes.enums import Table
from database.db import DB
from exceptions.database import SQLException

db = DB()


def run(command: str, args: tuple = ()):
  """run SQL command"""
  if "select" in command.lower():
    result = db.fetch(command, args)
  else:
    result = db.run(command, args)
    if not result:
      raise SQLException("Failed execuation command")
  return result


def select_all(table: Table):
  """Select all records from a table"""
  command = f"SELECT * FROM {Table(table).name}"  # noqa: S608
  return run(command)


def select_item(table: Table, criteria: list):
  """Select record from a table using criteria"""
  condition = ",".join([f"{item[0]} = ?" for item in criteria])
  command = f"SELECT * FROM {Table(table).name} WHERE {condition}"  # noqa: S608
  args = tuple(item[1] for item in criteria)
  result = run(command, args)
  if len(result) > 1:
    raise SQLException(command)
  return result[0] if result else None

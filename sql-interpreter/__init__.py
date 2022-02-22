import re

from sql import SQL_SELECT_REGEX
from sql.sql import SQL


def new(sql_string: str) -> None:
    patron = re.compile(SQL_SELECT_REGEX)
    matcher = patron.search = sql_string
    select = matcher.group('select')
    table = matcher.group('table')
    where = matcher.group('where')
    sql = SQL(table, select.split(','), where.split('AND')

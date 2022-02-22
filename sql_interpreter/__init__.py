import re

"""from sql_interpreter.sql import (SQL_REGEX_SELECT_WITH_WHERE,
                                 SQL_REGEX_SELECT_WITH_SUBQUERY,
                                 SQL_REGEX_SELECT)
"""
from sql_interpreter.sql.sql import SQL


def new(sql_string: str) -> None:
    """sql_regexs = [SQL_REGEX_SELECT_WITH_SUBQUERY, SQL_REGEX_SELECT_WITH_WHERE,
                  SQL_REGEX_SELECT]
    for regex in sql_regexs:
        patron = re.compile(regex, re.I)
        matcher = patron.search(sql_string)
        if matcher is not None:
            break"""
    select = matcher.group('select')
    table = matcher.group('table')
    where = matcher.group('where')
    sql = SQL(table, select.split(','), where.split('AND'))
    print(f'Table: {sql.table}')
    print(f'Columns: {sql.select}')
    print(f'Where: {sql.where}')

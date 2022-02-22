import re

from sql_interpreter.sql import SQL_REGEX_COLUMN, SQL_REGEX_COLUMN_ALIAS


class Column:
    def __init__(self, columns_str: str) -> None:
        if 'as' in columns_str.lower():
            patron = re.compile(SQL_REGEX_COLUMN_ALIAS, re.I)
            matcher = patron.search(columns_str)
            self.column = matcher.group('column')
            self.alias = matcher.group('alias')
        else:
            patron = re.compile(SQL_REGEX_COLUMN, re.I)
            matcher = patron.search(columns_str)
            self.column = matcher.group('column')
            self.alias = None

    def __str_(self):
        if self.alias is None:
            return f'{self.column}'
        else:
            return f'{self.column} as {self.alias}'

    def __repr__(self):
        if self.alias is None:
            return f'{self.column}'
        else:
            return f'{self.column} as {self.alias}'



SQL_REGEX_SELECT = "SELECT([ ]+)(?P<select>[A-Za-z0-9_\W*]*)([ ]+)FROM([ ]+)(?P<table>[A-Za-z0-9_\W*]*)"

SQL_REGEX_SELECT_WITH_WHERE = "SELECT([ ]+)(?P<select>[A-Za-z0-9_\W*]*)([ ]+)FROM([ ]+)(?P<table>[A-Za-z0-9_\W*]*)([ ]+)WHERE([ ]+)(?P<where>[A-Za-z0-9_\W*]*)"

SQL_REGEX_SELECT_WITH_SUBQUERY = "SELECT([ ]+)(?P<select>[A-Za-z0-9_\W*]*)([ ]+)FROM([ ]+)\((?P<table>[A-Za-z0-9_\W*]*)\)([ ]+)WHERE([ ]+)(?P<where>[A-Za-z0-9_\W*]*)"


SQL_REGEX_COLUMN = '(?P<column>[A-Za-z0-9_\W*]*)'
SQL_REGEX_COLUMN_ALIAS = '(?P<column>[A-Za-z0-9_\W*]*) as (?P<alias>[A-Za-z0-9_\W*]*)'

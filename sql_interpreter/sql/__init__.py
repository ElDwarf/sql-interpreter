SQL_REGEX_SELECT = "SELECT([ ]+)(?P<select>[A-Za-z0-9_\W*]*)([ ]+)FROM"

SQL_REGEX_FROM = "FROM([ ]+)([/(]?)(?P<table>[A-Za-z0-9_\W*]*)([/)]?)(([ ]+)LEFT([ ]+)JOIN(.*)|([ ]+)INNER([ ]+)JOIN(.*)|([ ]+)RIGHT([ ]+)JOIN(.*)|([ ]+)WHERE(.*)|([ ]+)GROUP(.*)|([ ]+)ORDER(.*)|$)"

SQL_REGEX_JOIN = "(?P<join>LEFT([ ]+)JOIN(.*)|INNER([ ]+)JOIN(.*)|RIGHT([ ]+)JOIN(.*))([ ]+)WHERE(.*)|([ ]+)GROUP(.*)|([ ]+)ORDER(.*)|$"

# En proceso no funciona todavia
SQL_REGEX_WHERE = "WHERE[ ]+(?P<where>(.*))([ ]+)GROUP(.*)|([ ]+)ORDER(.*)|$"

SQL_REGEX_GROUP = "GROUP(?P<group>(.*))([ ]+)ORDER(.*)|$"

SQL_REGEX_ORDER = "ORDER(?P<oder>(.*))([ ]+)GROUP(.*)|$"




SQL_REGEX_COLUMN = '(?P<column>[A-Za-z0-9_\W*]*)'
SQL_REGEX_COLUMN_ALIAS = '(?P<column>[A-Za-z0-9_\W*]*) as (?P<alias>[A-Za-z0-9_\W*]*)'

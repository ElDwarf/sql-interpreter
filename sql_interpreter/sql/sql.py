from sql_interpreter.sql.select_component import Column


class SQL():
    def __init__(self, table: str=None, select: list[str]=[], where: list[str]=[],
                 post_process: list[str]=[]) -> None:
        self.table = table
        self.select = self.__process_columns(select)
        self.where = where
        self.post_process = post_process

    def __process_columns(self, columns: list[str]) -> list[Column]:
        response = []
        for column in columns:
            response.append(Column(column))
        return response


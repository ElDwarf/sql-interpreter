class SQL():

    def __init__(table: str=None, select: list(str)=[], where: list(str)=[],
                 post_process: list(str)=[]) -> None:
        self.table = table
        self.select = select
        self.where = where
        self.post_process = post_process

import uuid


class tech_func:
    def __init__(self):
        pass

    @staticmethod
    def capitalize2(string_col: str):
        return string_col.capitalize()

    @staticmethod
    def gen_uid():
        return uuid.uuid4()

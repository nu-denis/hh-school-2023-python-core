class Beer:
    def __init__(self, title=None, production_date=None) -> None:
        # TODO: добавить инициализацию
        self.title = title
        self.production_date = production_date

    def __str__(self):
        return f"Beer: {self.title}, Production Date: {self.production_date}"

        # pass



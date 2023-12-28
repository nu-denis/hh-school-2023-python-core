from datetime import date


class Drink:
    def __init__(self, title: str = None, production_date: date = None) -> None:
        self.title = title
        self.production_date = production_date

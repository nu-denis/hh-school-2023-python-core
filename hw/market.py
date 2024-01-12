from decorator import log_execution_time
class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        if wines is None:
            wines = []
        if beers is None:
            beers = []
        all_drinks = wines + beers
        self.all_drinks_by_title = {drink.title: drink for drink in all_drinks}
        self.all_drinks_sorted_by_title = sorted(all_drinks, key=lambda drink: drink.title)

    @log_execution_time
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)
        :param title:
        :return: True|False
        """
        return title in self.all_drinks_by_title

    @log_execution_time
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        # return list(self.all_drinks_sorted_by_title)
        return [*self.all_drinks_sorted_by_title]

    @log_execution_time
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        if from_date is None:
            from_date = '0000.00.00'
        if to_date is None:
            to_date = '9999.99.99'
        return [
            drink for drink in self.all_drinks_sorted_by_title
            if from_date <= drink.production_date <= to_date
        ]

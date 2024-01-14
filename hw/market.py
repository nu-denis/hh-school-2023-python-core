from logger import timing_decorator
import time

class Market:

    drinks = {}

    def __init__(self, wines: list = None, beers: list = None) -> None:
        if wines:
            self.drinks.update({wine.title: wine for wine in wines})
        if beers:
            self.drinks.update({beer.title: beer for beer in beers})

    @timing_decorator
    def has_drink_with_title(self, title=None) -> bool:
        return title in self.drinks

    @timing_decorator
    def get_drinks_sorted_by_title(self) -> list:
        return sorted(self.drinks.values(), key=lambda drink: drink.title)

    @timing_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        time.sleep(1) # задержка выполнения в 1 секунду для демонстрации работы декоратора
        if from_date and to_date:
            return [drink for drink in self.drinks.values() if from_date <= drink.production_date <= to_date]
        else:
            return []

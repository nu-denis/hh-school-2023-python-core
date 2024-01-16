from datetime import datetime

def function_info_decorator(func):
    def wrapper(*args, **kwargs):
        print('\nСтарт функции', func.__qualname__)
        start = datetime.now()
        result = func(*args, **kwargs)
        print('Финиш. Затраченное время: ', datetime.now() - start)
        print('Результат выполнения:\n', result)
        return result
    return wrapper

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = { drink.title: drink for drink in wines }
        self.beers = { drink.title: drink for drink in beers }

    @function_info_decorator
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.wines or title in self.beers

    @function_info_decorator
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted([*self.beers, *self.wines], key=lambda x: (x is None, x))

    @function_info_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        drinks = [*self.beers.values(), *self.wines.values()]
        filtered_drinks =  list(filter(lambda drink: self.__date_in_range(drink, from_date, to_date), drinks))
        result = list()

        for drink in filtered_drinks:
            result.append(drink.title)

        return result

    def __date_in_range(self, drink, from_date=None, to_date=None) -> bool:
        """
        Метод проверяющий входит ли production_date в from_date : to_date

        :return: bool
        """
        if drink.production_date is None:
            return False

        if not from_date and not to_date:
            return True
        
        if not from_date:
            return drink.production_date <= to_date
        
        if not to_date:
            return drink.production_date >= from_date

        return from_date <= drink.production_date <= to_date
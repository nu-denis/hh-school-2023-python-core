from wine import Wine
from beer import Beer
from market import Market
from random import randint, shuffle

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""

vkusvill = Market(
    wines=[
        Wine("vine 1", 2024),
        Wine("vine 2", 2023),
        Wine("vine 4", 2022),
        Wine("vine 7", 2021),
        Wine("vine 3", 2020),
        Wine("vine 6", 2020),
    ],
    beers=[
        Beer("beer 1", 2022),
        Beer("beer 3", 2022),
        Beer("beer 2", 2021),
        Beer(None, 2021),
        Beer("beer 4", None),
    ]
)

vkusvill.has_drink_with_title('vine 1')
vkusvill.has_drink_with_title('vine 11')
vkusvill.get_drinks_by_production_date(None,2023)
vkusvill.get_drinks_by_production_date(2021,None)
vkusvill.get_drinks_by_production_date(None,None)
vkusvill.get_drinks_sorted_by_title()
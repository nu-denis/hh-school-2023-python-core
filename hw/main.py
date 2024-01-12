from datetime import datetime
from wine import Wine
from beer import Beer
from market import Market


wine1 = Wine("Merlot", "2023.01.17")
wine2 = Wine("Chardonnay", "2022.05.03")
# wine1 = Wine["Chardonnay", "2022.05.03"]


beer1 = Beer("Stout", "2022.02.10")
beer2 = Beer("IPA", "2023.03.04")

market = Market(wines=[wine1, wine2], beers=[beer1, beer2])

# проверка наличия напитка по наименованию
print(market.has_drink_with_title("Merlot"))
print(market.has_drink_with_title("Merlot07"))

# получение отсортированного списка напитков по наименованию
print('По наименованию:')
sorted_drinks = market.get_drinks_sorted_by_title()
# print(*map(lambda drink: drink.title, sorted_drinks), sep='; ')
for drink in sorted_drinks:
    print(drink)

# получение списка напитков по дате производства
print('По дате:')
drinks_by_date = market.get_drinks_by_production_date("2023.01.01", "2023.04.01")
for drink in drinks_by_date:
    print(drink)


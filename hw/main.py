from wine import Wine
from beer import Beer
from market import Market

wines = [
    Wine("Кокур десертный Сурож", "2020-10-17"),
    Wine("Пино Гри Ай-Даниль", "2014-05-11"),
    Wine("Мускат белый десертный", "2015-12-01"),
    Wine("Херес", "2022-07-30")
]

beers = [
    Beer("Жигулевское", "2020-10-17"),
    Beer("Девятка", "2014-05-11"),
    Beer("Хугарден Бланш", "2015-12-01"),
    Beer("Альтбир", "2022-07-30")
]

market = Market(wines, beers)

print("\n--------- Отсортированный список напитков ---------\n")
for drink in market.get_drinks_sorted_by_title():
    print(drink.title)

print("\n--------- Проверить наличие пива КЕК ---------\n")
print(market.has_drink_with_title("КЕК"))
print("\n--------- Проверить наличие вина Херес ---------\n")
print(market.has_drink_with_title("Херес"))

print("\n--------- Список напитков за 2014-2015 гг. ---------\n")
drinks_in_date_range = market.get_drinks_by_production_date("2014-01-01", "2015-12-31")
for drink in drinks_in_date_range:
    print(drink.title)

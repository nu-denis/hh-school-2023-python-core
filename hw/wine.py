from drink import Drink


class Wine(Drink):
    def __str__(self):
        return f'Wine: (Title: {self.title}, Production date: {self.production_date})'

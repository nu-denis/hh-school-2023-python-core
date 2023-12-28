from drink import Drink


class Beer(Drink):
    def __str__(self):
        return f'Beer: (Title: {self.title}, Production date: {self.production_date})'

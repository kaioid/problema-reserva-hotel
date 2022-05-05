class Hotel:
    def __init__(self, name, rating, price_card):
        self.__name = name
        self.__rating = rating
        self.__price_card = price_card

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def price_card(self):
        catalog = []
        for value in self.__price_card:
            catalog.append(self.__price_card[value])
        return catalog



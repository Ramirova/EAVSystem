import Location


class Building(Location):

    def __init__(self, longitude, latitude, street, number):
        Location.__init__(self, longitude, latitude)
        self.street = street
        self.number = number

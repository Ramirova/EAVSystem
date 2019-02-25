import Location


class Building:

    def __init__(self, longitude, latitude, street, number):
        self.location = Location(longitude, latitude)
        self.street = street
        self.number = number

import Location


class PublicTransportStop:

    def __init__(self, longitude, latitude, street, name):
        self.location = Location(longitude, latitude)
        self.name = name
        self.street = street
        self.number = number



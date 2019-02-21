import Location


class Public_transport_stop(Location):

    def __init__(self, longitude, latitude, name, street):
        self.name = name
        Location.__init__(self, longitude, latitude)
        self.street = street



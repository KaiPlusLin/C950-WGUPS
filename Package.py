

#Create a Package object with variables
class Package:
    def __init__(self, id, address, city, state, zip_code, delivery_deadline, weight, special_notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes

        self.delivery_time = None
        self.delivery_status = "Hub"

    def __str__(self):
        return (f"Package(id={self.id}, address='{self.address}', city='{self.city}', "
                f"state='{self.state}', zip_code='{self.zip_code}', "
                f"delivery_deadline='{self.delivery_deadline}', weight={self.weight}, "
                f"special_notes='{self.special_notes}, "
                f"delivery_time='{self.delivery_time}, "
                f"delivery_status='{self.delivery_status}")
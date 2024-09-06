#Create a Package object with variables
class Package:
    def __init__(self, id, address, city, state, zipe_code, delivery_time, date, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zipe_code
        self.delivery_time = delivery_time
        self.date = date
        self.status = status
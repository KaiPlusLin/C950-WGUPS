

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
        self.delivery_status = "HUB"
        self.truck_number = None

    def __str__(self):
        return (f"Package id: {self.id}, Address: {self.address}, City: {self.city}, "
                f"State: {self.state}, Zipcode: {self.zip_code}, "
                f"Delivery Deadline: {self.delivery_deadline}, Weight: {self.weight}, "
                f"Special Notes: {self.special_notes}, "
                f"Delivery Time: {self.delivery_time}, "
                f"Delivery Status {self.delivery_status}, Truck {self.truck_number}")
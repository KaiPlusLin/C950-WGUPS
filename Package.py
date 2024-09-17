from datetime import timedelta


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
        self.departure_time = None

    def __str__(self):
        return (f"Package id: {self.id}, Address: {self.address}, City: {self.city}, "
                f"State: {self.state}, Zipcode: {self.zip_code}, "
                f"Delivery Deadline: {self.delivery_deadline}, Weight: {self.weight}, "
                # f"Special Notes: {self.special_notes}, "
                f"Delivery Time: {self.delivery_time}, "
                f"Delivery Status {self.delivery_status}, Truck {self.truck_number}")

    def status(self, time_entered):
        temp_status = "Enroute"
        if time_entered > self.delivery_time:
            temp_status = "Delivered"

        elif time_entered < self.departure_time:
            temp_status = "At Hub"

        temp_address = self.address
        temp_zip = self.zip_code

        if self.id == 9 and time_entered >= timedelta(hours=10, minutes=20):
            temp_address = "410 S State St"
            temp_zip = "84111"


        return (f"ID: {self.id}- Address: {temp_address}, {self.city}, "
                f"{self.state}, {temp_zip} "
                f"Due by: {self.delivery_deadline} Weight: {self.weight} "
                f"Special Notes: {self.special_notes} "
                f"Delivery Time: {self.delivery_time} "
                f"Status: {temp_status} Truck: {self.truck_number}")



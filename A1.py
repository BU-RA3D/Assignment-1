# Creating Python classes for the identified classes in the hotel reservation system

class Reservation:
    def __init__(self, reservation_id, customer_details, room_type, check_in_date, check_out_date):
        self.__reservation_id = reservation_id
        self.__customer_details = customer_details
        self.__room_type = room_type
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date

    # Getter and Setter for reservation_id
    def get_reservation_id(self):
        return self.__reservation_id

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    # Getter and Setter for customer_details
    def get_customer_details(self):
        return self.__customer_details

    def set_customer_details(self, customer_details):
        self.__customer_details = customer_details

    # Getter and Setter for room_type
    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    # Getter and Setter for check_in_date
    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    # Getter and Setter for check_out_date
    def get_check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    # Function headers with pass
    def create_reservation(self):
        """Creates a new reservation."""
        pass

    def modify_reservation(self):
        """Modifies the reservation details."""
        pass

    def cancel_reservation(self):
        """Cancels the reservation."""
        pass


class Payment:
    def __init__(self, payment_id, amount, payment_method, reservation_id, customer_id):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__payment_method = payment_method
        self.__reservation_id = reservation_id
        self.__customer_id = customer_id

    # Getter and Setter for payment_id
    def get_payment_id(self):
        return self.__payment_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    # Getter and Setter for amount
    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    # Getter and Setter for payment_method
    def get_payment_method(self):
        return self.__payment_method

    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

    # Getter and Setter for reservation_id
    def get_reservation_id(self):
        return self.__reservation_id

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    # Getter and Setter for customer_id
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    # Function headers with pass
    def process_payment(self):
        """Processes the payment for the reservation."""
        pass


class Customer:
    def __init__(self, customer_id, name, email, phone_number, address):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address

    # Getter and Setter for customer_id
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter for email
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # Getter and Setter for phone_number
    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # Getter and Setter for address
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    # Function headers with pass
    def make_reservation(self):
        """Initiates the reservation process."""
        pass

    def modify_reservation(self, reservation_id):
        """Modifies an existing reservation."""
        pass

    def cancel_reservation(self, reservation_id):
        """Cancels an existing reservation."""
        pass


class Room:
    def __init__(self, room_number, room_type, is_available, price_per_night, amenities):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__is_available = is_available
        self.__price_per_night = price_per_night
        self.__amenities = amenities

    # Getter and Setter for room_number
    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    # Getter and Setter for room_type
    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    # Getter and Setter for is_available
    def get_is_available(self):
        return self.__is_available

    def set_is_available(self, is_available):
        self.__is_available = is_available

    # Getter and Setter for price_per_night
    def get_price_per_night(self):
        return self.__price_per_night

    def set_price_per_night(self, price_per_night):
        self.__price_per_night = price_per_night

    # Getter and Setter for amenities
    def get_amenities(self):
        return self.__amenities

    def set_amenities(self, amenities):
        self.__amenities = amenities

    # Function headers with pass
    def check_availability(self):
        """Checks if the room is available."""
        pass

    def reserve_room(self):
        """Reserves the room for a customer."""
        pass


# Creating objects for each class and populating them with data from the example reservation

# Creating a Customer object
customer = Customer(customer_id=1, name="Ted Vera", email="tedvera@mac.com", phone_number="555-661-1110", address="2455 Trinity Drive, Los Alamos, NM 87544")

# Creating a Reservation object
reservation = Reservation(reservation_id=62523687, customer_details="Ted Vera", room_type="2 Queen Beds / No Smoking / Desk / Safe / Coffee Maker / Hair Dryer", check_in_date="Sun, Aug 22, 2010 - 03:00 PM", check_out_date="Tue, Aug 24, 2010 - 12:00 PM")

# Creating a Room object
room = Room(room_number=1, room_type="2 Queen Beds", is_available=True, price_per_night=89.95, amenities="No Smoking, Desk, Safe, Coffee Maker, Hair Dryer")

# Creating a Payment object
payment = Payment(payment_id=9904, amount=201.48, payment_method="Mastercard (ending in 9904)", reservation_id=62523687, customer_id=1)

# Displaying the populated information

print("Customer Information:")
print(f"Name: {customer.get_name()}")
print(f"Email: {customer.get_email()}")
print(f"Phone Number: {customer.get_phone_number()}")
print(f"Address: {customer.get_address()}\n")

print("Reservation Details:")
print(f"Reservation ID: {reservation.get_reservation_id()}")
print(f"Customer: {reservation.get_customer_details()}")
print(f"Room Type: {reservation.get_room_type()}")
print(f"Check-In Date: {reservation.get_check_in_date()}")
print(f"Check-Out Date: {reservation.get_check_out_date()}\n")

print("Room Information:")
print(f"Room Number: {room.get_room_number()}")
print(f"Room Type: {room.get_room_type()}")
print(f"Price Per Night: ${room.get_price_per_night()}")
print(f"Amenities: {room.get_amenities()}\n")

print("Payment Details:")
print(f"Payment ID: {payment.get_payment_id()}")
print(f"Payment Method: {payment.get_payment_method()}")
print(f"Amount: ${payment.get_amount()}")

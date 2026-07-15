import logging

logging.basicConfig(
    filename='bookings.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class Room:
    def __init__(self, room_number: int, room_type: str, price_per_night: float, max_guests: int):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True
        self.max_guests = max_guests

    def book_room(self):
        if not self.is_available:
            raise ValueError(f"Room {self.room_number} is already booked")
        self.is_available = False

    def release_room(self):
        self.is_available = True

    def calculate_price(self, nights: int) -> float:
        base_price = self.price_per_night * nights
        if nights >= 5:
            return base_price * 0.9
        return base_price

    def __str__(self):
        status = "Available" if self.is_available else "Occupied"
        return f"Room #{self.room_number} ({self.room_type}) - ${self.price_per_night}/night | Status: {status} | Max Guests: {self.max_guests}"


class Customer:
    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget
        self.booked_rooms = []
        self.reward_points = 0

    def add_room(self, room: Room):
        if room not in self.booked_rooms:
            self.booked_rooms.append(room)

    def remove_room(self, room: Room):
        if room in self.booked_rooms:
            self.booked_rooms.remove(room)

    def pay_for_booking(self, total_price: float) -> bool:
        if self.budget >= total_price:
            self.budget -= total_price
            earned_points = int(total_price // 10)
            self.reward_points += earned_points
            return True
        return False

    def show_booking_summary(self) -> str:
        if not self.booked_rooms:
            return f"Customer {self.name} has no active bookings."
        rooms_list = ", ".join([f"#{r.room_number}" for r in self.booked_rooms])
        return f"Customer: {self.name} | Booked Rooms: [{rooms_list}] | Balance: ${self.budget} | Reward Points: {self.reward_points}"


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.bookings_log = []

    def add_room_to_hotel(self, room: Room):
        self.rooms.append(room)

    def show_available_rooms(self, room_type: str = None) -> list:
        available = [room for room in self.rooms if room.is_available]
        if room_type:
            available = [room for room in available if room.room_type.lower() == room_type.lower()]
        return available

    def calculate_total_booking(self, room_number: int, nights: int) -> float:
        for room in self.rooms:
            if room.room_number == room_number:
                return room.calculate_price(nights)
        raise ValueError("Room with the specified number was not found")

    def log_booking(self, customer: Customer, room: Room, total_price: float):
        log_message = f"Customer {customer.name} booked Room #{room.room_number} | Paid: ${total_price}"
        self.bookings_log.append(log_message)
        logging.info(log_message)

    def book_room_for_customer(self, customer: Customer, room_number: int, nights: int) -> bool:
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_available:
                    print(f"Room #{room_number} is already occupied!")
                    return False
                
                total_price = room.calculate_price(nights)
                if customer.pay_for_booking(total_price):
                    room.book_room()
                    customer.add_room(room)
                    self.log_booking(customer, room, total_price)
                    print(f"Booking successful! Paid: ${total_price}")
                    return True
                else:
                    print(f"Insufficient funds! Required: ${total_price}, Your Balance: ${customer.budget}")
                    return False
        
        print("Room not found")
        return False

    def cancel_booking(self, customer: Customer, room_number: int):
        for room in customer.booked_rooms:
            if room.room_number == room_number:
                room.release_room()
                customer.remove_room(room)
                log_message = f"Customer {customer.name} canceled booking for Room #{room_number}"
                self.bookings_log.append(log_message)
                logging.info(log_message)
                print(f"Booking for Room #{room_number} has been canceled")
                return True
        print("This room is not booked by this customer")
        return False

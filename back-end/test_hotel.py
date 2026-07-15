import unittest
from hotel_booking import Room, Customer, Hotel

class TestHotelBookingSystem(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel("Sheraton")
        self.room1 = Room(101, "Single", 100.0, 1)
        self.room2 = Room(102, "Double", 180.0, 2)
        self.hotel.add_room_to_hotel(self.room1)
        self.hotel.add_room_to_hotel(self.room2)
        
        self.customer_rich = Customer("George", 500.0)
        self.customer_poor = Customer("Anna", 50.0)

    def test_pay_for_booking_success_and_reduction(self):
        """Tests that the budget is correctly reduced after a successful payment"""
        initial_budget = self.customer_rich.budget
        payment_amount = 150.0
        
        success = self.customer_rich.pay_for_booking(payment_amount)
        
        self.assertTrue(success)
        self.assertEqual(self.customer_rich.budget, initial_budget - payment_amount)
        self.assertEqual(self.customer_rich.reward_points, 15)

    def test_pay_for_booking_insufficient_funds(self):
        """Tests that payment is rejected when the customer has insufficient funds"""
        initial_budget = self.customer_poor.budget
        payment_amount = 100.0
        
        success = self.customer_poor.pay_for_booking(payment_amount)
        
        self.assertFalse(success)
        self.assertEqual(self.customer_poor.budget, initial_budget)

    def test_book_room_for_customer_success(self):
        """Tests a successful booking of an available room"""
        self.assertTrue(self.room1.is_available)
        
        success = self.hotel.book_room_for_customer(self.customer_rich, 101, 1)
        
        self.assertTrue(success)
        self.assertFalse(self.room1.is_available)
        self.assertIn(self.room1, self.customer_rich.booked_rooms)

    def test_book_already_booked_room(self):
        """Tests that booking an already occupied room is not allowed"""
        self.hotel.book_room_for_customer(self.customer_rich, 101, 1)
        
        another_customer = Customer("David", 1000.0)
        success = self.hotel.book_room_for_customer(another_customer, 101, 1)
        
        self.assertFalse(success)
        self.assertNotIn(self.room1, another_customer.booked_rooms)

    def test_cancel_booking(self):
        """Tests canceling a booking and releasing the room back to available status"""
        self.hotel.book_room_for_customer(self.customer_rich, 101, 1)
        self.assertFalse(self.room1.is_available)
        
        cancel_success = self.hotel.cancel_booking(self.customer_rich, 101)
        
        self.assertTrue(cancel_success)
        self.assertTrue(self.room1.is_available)
        self.assertNotIn(self.room1, self.customer_rich.booked_rooms)

if __name__ == '__main__':
    unittest.main()

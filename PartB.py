# PartB.py
"""
Unit tests for the Part A implementation.
"""

import unittest
from PartA import House, Penthouse

class TestHouse(unittest.TestCase):
    def setUp(self):
        # Initialse a House object for testing.
        self.house = House("123", "Parnell Street", "Suburb", 5, 500000.00)
    
    def test_instance_of_house(self):
        # Confirm the object is an instance of House.
        self.assertIsInstance(self.house, House)
    
    def test_not_instance_of_penthouse(self):
        # Confirm the House object is not an instance of Penthouse.
        self.assertNotIsInstance(self.house, Penthouse)
    
    def test_update_methods_house(self):
        # Test that the update methods for House work correctly.
        self.house.update_house_number("999")
        self.assertEqual(self.house.house_number, "999")
        
        self.house.update_street("Queen Street")
        self.assertEqual(self.house.street, "Queen Street")
        
        self.house.update_area("Urban")
        self.assertEqual(self.house.area, "Urban")
        
        self.house.update_number_of_beds(7)
        self.assertEqual(self.house.number_of_beds, 7)
        
        self.house.update_price(750000.00)
        self.assertEqual(self.house.price, 750000.00)
    
    def test_identity_house(self):
        # Test that two references to the same House object are identical.
        house_copy = self.house
        self.assertIs(self.house, house_copy)
        
        # Create a new House object with the same values; they should not be identical.
        another_house = House("123", "Parnell Street", "Suburb", 5, 500000.00)
        self.assertIsNot(self.house, another_house)

class TestPenthouse(unittest.TestCase):
    def setUp(self):
        # Initialse a Penthouse object for testing.
        self.penthouse = Penthouse("456", "Parnell Street", "Suburb", 5, 500000.00, 25, True)
    
    def test_instance_of_penthouse(self):
        # Confirm the object is an instance of Penthouse.
        self.assertIsInstance(self.penthouse, Penthouse)
    
    def test_instance_of_house(self):
        # Confirm that a Penthouse is also an instance of House (inheritance).
        self.assertIsInstance(self.penthouse, House)
    
    def test_update_methods_penthouse(self):
        # Test that the update methods for Penthouse work correctly.
        self.penthouse.update_floor_number(30)
        self.assertEqual(self.penthouse.floor_number, 30)
        
        self.penthouse.update_has_roof_terrace(False)
        self.assertEqual(self.penthouse.has_roof_terrace, False)
    
    def test_identity_penthouse(self):
        # Test that two references to the same Penthouse object are identical.
        penthouse_copy = self.penthouse
        self.assertIs(self.penthouse, penthouse_copy)
        
        # Create a new Penthouse with the same values; they should not be identical.
        another_penthouse = Penthouse("456", "Parnell Street", "Suburb", 5, 500000.00, 25, True)
        self.assertIsNot(self.penthouse, another_penthouse)

if __name__ == '__main__':
    # Run all unit tests.
    unittest.main()

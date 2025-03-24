# PartA.py
# This file implements Part A of the exam for a House class (assigned based on student number b00143913)
# Attributes for House: house_number, street, area, number_of_beds, price

class House:
    def __init__(self, house_number, street, area, number_of_beds, price):
        # Initialise the House object with the given attributes.
        # Type assumptions: house_number (str), street (str), area (str), number_of_beds (int), price (float)
        if not isinstance(house_number, str):
            raise TypeError("house_number must be a string")
        if not isinstance(street, str):
            raise TypeError("street must be a string")
        if not isinstance(area, str):
            raise TypeError("area must be a string")
        if not isinstance(number_of_beds, int):
            raise TypeError("number_of_beds must be an integer")
        if not (isinstance(price, float) or isinstance(price, int)):
            raise TypeError("price must be a number (float or int)")

        self.house_number = house_number
        self.street = street
        self.area = area
        self.number_of_beds = number_of_beds
        self.price = float(price)

    def print_attributes(self):
        # Print all initialisation attributes of the House.
        print("House Attributes:")
        print(f"House Number: {self.house_number}")
        print(f"Street: {self.street}")
        print(f"Area: {self.area}")
        print(f"Number of Beds: {self.number_of_beds}")
        print(f"Price: {self.price}")

    # Update methods with type checking.
    def update_house_number(self, new_house_number):
        if not isinstance(new_house_number, str):
            raise TypeError("new_house_number must be a string")
        self.house_number = new_house_number

    def update_street(self, new_street):
        if not isinstance(new_street, str):
            raise TypeError("new_street must be a string")
        self.street = new_street

    def update_area(self, new_area):
        if not isinstance(new_area, str):
            raise TypeError("new_area must be a string")
        self.area = new_area

    def update_number_of_beds(self, new_number_of_beds):
        if not isinstance(new_number_of_beds, int):
            raise TypeError("new_number_of_beds must be an integer")
        self.number_of_beds = new_number_of_beds

    def update_price(self, new_price):
        if not (isinstance(new_price, float) or isinstance(new_price, int)):
            raise TypeError("new_price must be a number (float or int)")
        self.price = float(new_price)

# Child class (Penthouse) with extra attributes.
class Penthouse(House):
    def __init__(self, house_number, street, area, number_of_beds, price, floor_number, has_roof_terrace):
        # Initialise the parent House attributes.
        super().__init__(house_number, street, area, number_of_beds, price)
        # Extra attributes for Penthouse:
        # floor_number (int): the floor number of the penthouse.
        # has_roof_terrace (bool): whether the penthouse has a roof terrace.
        if not isinstance(floor_number, int):
            raise TypeError("floor_number must be an integer")
        if not isinstance(has_roof_terrace, bool):
            raise TypeError("has_roof_terrace must be a boolean")
        self.floor_number = floor_number
        self.has_roof_terrace = has_roof_terrace

    def print_penthouse_attributes(self):
        # Print all attributes from House plus the extra Penthouse attributes.
        print("Penthouse Attributes:")
        self.print_attributes()  # Print parent attributes.
        print(f"Floor Number: {self.floor_number}")
        print(f"Has Roof Terrace: {self.has_roof_terrace}")

    # Update methods for extra attributes.
    def update_floor_number(self, new_floor_number):
        if not isinstance(new_floor_number, int):
            raise TypeError("new_floor_number must be an integer")
        self.floor_number = new_floor_number

    def update_has_roof_terrace(self, new_has_roof_terrace):
        if not isinstance(new_has_roof_terrace, bool):
            raise TypeError("new_has_roof_terrace must be a boolean")
        self.has_roof_terrace = new_has_roof_terrace

# Demonstration of tasks A8-A10.
if __name__ == "__main__":
    # Create an instance of House with the updated values.
    my_house = House("123", "Parnell Street", "Suburb", 5, 500000.00)
    my_house.print_attributes()  # A3

    # Create an instance of Penthouse (child class) with updated values.
    my_penthouse = Penthouse("456", "Parnell Street", "Suburb", 5, 500000.00, 25, True)
    my_penthouse.print_penthouse_attributes()  # A6

    # Demonstrate update methods for House (A4) with new example values.
    print("\nUpdating House attributes:")
    my_house.update_house_number("999")
    my_house.update_street("Queen Street")
    my_house.update_area("Urban")
    my_house.update_number_of_beds(7)
    my_house.update_price(750000.00)
    my_house.print_attributes()

    # Demonstrate update methods for Penthouse extra attributes (A7) with new example values.
    print("\nUpdating Penthouse extra attributes:")
    my_penthouse.update_floor_number(30)
    my_penthouse.update_has_roof_terrace(False)
    my_penthouse.print_penthouse_attributes()

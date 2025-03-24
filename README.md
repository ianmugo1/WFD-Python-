# Part A Implementation

This part of the project implements two Python classes:

- **House**  
  A class with attributes for house number, street, area, number of beds, and price. It includes methods to print these attributes and update each one with proper type checking.

- **Penthouse**  
  A subclass of House that adds extra attributes (floor number and whether it has a roof terrace). It provides its own print and update methods for these additional attributes.

This serves as the foundation for parts B and C of the project.

Part B: Unit Testing

This file (PartB.py) contains tests for the House and Penthouse classes from Part A. It uses Python’s built-in unittest module.

The tests check that:

A House object is created correctly.
A House object is not mistaken for a Penthouse.
The update methods change the values as expected.
Two references to the same object are the same, and new objects are different.
These tests help to make sure the code from Part A works correctly.

---

# Part C: Django Models

This file (models.py) has Django models for a car dealership. It defines the following models:

- **Car:** Represents a car with details like serial number, make, model, colour, year, and whether it is for sale.
- **Salesperson:** Stores the first and last name of a salesperson.
- **Customer:** Contains customer details such as first name, last name, phone number, address, city, state/province, and postal code.
- **SalesInvoice:** Links a car, a customer, and a salesperson. Each car can have one invoice.
- **Mechanic:** Represents a mechanic with a first and last name.
- **ServiceTicket:** Records a service job for a car, with extra details like comments and the date returned to the customer.
- **ServiceMechanic:** Connects mechanics and service tickets. This model shows that many mechanics can work on a ticket and one ticket can have many mechanics.
- **Part:** Represents a car part with a unique part number, description, purchase price, and retail price.
- **PartsUsed:** Links parts to service tickets and records the number of parts used.

These models match the relationships shown in the ERD and form the basis for the car dealership application.
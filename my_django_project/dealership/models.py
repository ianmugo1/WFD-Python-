# models.py
"""
Django models for a Car Dealership based on the provided ERD.

This file defines the following entities:
- Car
- Salesperson
- Customer
- SalesInvoice
- Mechanic
- ServiceTicket
- ServiceMechanic (a linking model for a many-to-many relationship between Mechanic and ServiceTicket)
- Part
- PartsUsed (a linking model for a many-to-many relationship between Part and ServiceTicket)
"""

from django.db import models

class Car(models.Model):
    # Each car is identified by a unique serial number.
    serial_number = models.CharField(max_length=50, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    # Indicates whether the car is available for sale.
    for_sale = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - SN: {self.serial_number}"

class Salesperson(models.Model):
    # Represents a salesperson with their first and last name.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Customer(models.Model):
    # Contains details for a customer.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    eir_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SalesInvoice(models.Model):
    # Each car can have at most one invoice (one-to-one relationship).
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    # Optional fields (e.g. invoice_date, invoice_price) can be added if required.

    def __str__(self):
        return f"Invoice #{self.id} for {self.car}"

class Mechanic(models.Model):
    # Represents a mechanic.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
   

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ServiceTicket(models.Model):
    # A service ticket is linked to a specific car.
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)
    date_returned_to_customer = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Service Ticket #{self.id} for {self.car}"

class ServiceMechanic(models.Model):
    """
    This is a linking model to represent the many-to-many relationship
    between Mechanics and ServiceTickets.
    """
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    # Additional fields (e.g. hours worked or rate) can be added if specified.

    def __str__(self):
        return f"{self.mechanic} on {self.service_ticket}"

class Part(models.Model):
    # Each part is uniquely identified by its part number.
    part_number = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Part #{self.part_number}: {self.description}"

class PartsUsed(models.Model):
    """
    This linking model represents the many-to-many relationship between
    Parts and ServiceTickets, along with the quantity used.
    """
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    number_used = models.PositiveIntegerField(default=1)
    # You could also track the price charged for each part if needed.

    def __str__(self):
        return f"{self.number_used}x {self.part} on {self.service_ticket}"

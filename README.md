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
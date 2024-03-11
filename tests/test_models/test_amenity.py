#!/usr/bin/python3

"""
    this is a test for the amenity model.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        lets Test the  Amenity class
    """

    def test_Amenity_inheritence(self):
        """
            lets test if the Amenity class Inherits from BaseModel
        """        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """
            lets Test that Amenity class has the name attribute.
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """
            lets Test that Amenity class has the name attribute's type.
        """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)

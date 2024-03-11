#!/usr/bin/python3
"""Test for the console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """for class test console"""

    def create(self):
        """for create the intance"""
        return HBNBCommand()

    def test_quit(self):
        """ for the method quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """for the method EOF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))

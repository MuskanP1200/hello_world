"""
Unit tests for hello.py
"""

import unittest
from hello_world.hello import get_message

class TestHello(unittest.TestCase):
    
    def test_default_message(self):
        self.assertEqual(get_message(), "Hello, World!")

    def test_custom_message(self):
        self.assertEqual(get_message("Muskan"), "Hello, Muskan!")

    def test_empty_string(self):
        self.assertEqual(get_message(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()

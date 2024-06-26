#!/usr/bin/python3
"""Test file for do_creatae"""
import unittest
from console import HBNBCommand
from models import storage
from models.state import State
import os


class TestHBNBCreate(unittest.TestCase):
    """Tests for the 'create' command"""

    def setUp(self):
        """Set up the test case environment"""
        # This runs before each test
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after each test case"""
        # This runs after each test
        # Let's remove all created states
        for key in list(storage.all(State).keys()):
            storage.delete(storage.all(State)[key])
        storage.save()

    def test_create_state(self):
        """Test creating a new State"""
        # Try creating a new State
        state_name = "name=\"California\""
        result = self.console.onecmd(f"create State {state_name}")
        state_id = result.split("\n")[0]
        self.assertTrue(state_id in storage.all(State).keys())
        state = storage.all(State)[state_id]
        self.assertEqual(state.name, "California")

    def test_create_state_with_int_param(self):
        """Test creating a new State with an integer parameter"""
        # Try creating a new State with an integer parameter
        state_params = "name=\"California\" population=5000000"
        result = self.console.onecmd(f"create State {state_params}")
        state_id = result.split("\n")[0]
        self.assertTrue(state_id in storage.all(State).keys())
        state = storage.all(State)[state_id]
        self.assertEqual(state.name, "California")
        self.assertEqual(state.population, 5000000)

    def test_create_state_with_invalid_param(self):
        """Test creating a new State with an invalid parameter"""
        # Try creating a new State with an invalid parameter
        state_params = "name=\"California\" invalid_param=invalid"
        result = self.console.onecmd(f"create State {state_params}")
        state_id = result.split("\n")[0]
        self.assertTrue(state_id in storage.all(State).keys())
        state = storage.all(State)[state_id]
        # Make sure the invalid param wasn't set
        self.assertFalse(hasattr(state, 'invalid_param'))

    def test_create_state_with_float_param(self):
        """Test creating a new State with a float parameter"""
        # Try creating a new State with a float parameter
        state_params = "name=\"California\" area=423967.0"
        result = self.console.onecmd(f"create State {state_params}")
        state_id = result.split("\n")[0]
        self.assertTrue(state_id in storage.all(State).keys())
        state = storage.all(State)[state_id]
        self.assertEqual(state.name, "California")
        self.assertEqual(state.area, 423967.0)

if __name__ == "__main__":
    unittest.main()

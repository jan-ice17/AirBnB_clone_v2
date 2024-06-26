#!/usr/bin/python3
"""This is a unittest for the do_create method
in the console.py file.
"""

import unittest
import io
from unittest.mock import patch, MagicMock
from console import HBNBCommand
from models import storage, Place, State


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up the test environment"""

        self.console = HBNBCommand()
        self.storage_save_patch = patch('models.storage.save')
        self.mock_save = self.storage_save_patch.start()

    def tearDown(self):
        """Tear down the test environment"""

        self.storage_save_patch.stop()

    def test_create_no_class_name(self):
        """Test creating an object without a class name"""

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.console.do_create("")
            self.assertEqual(
                             mock_stdout.getvalue().strip(),
                             "** class name missing **"
            )

    def test_create_with_valid_params(self):
        """Test creating an object with valid parameters"""

        class_name = "Place"
        params = 'city_id="0001" user_id="0001" name="My_little_house"\
                  number_rooms=4\
                  number_bathrooms=2 max_guest=10 price_by_night=300\
                  latitude=37.773972 longitude=-122.431297'
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.console.do_create(f"{class_name} {params}")
            output = mock_stdout.getvalue().strip()
            # Check that an ID was printed
            self.assertTrue(len(output) > 0)

        instance_id = output
        mock_instance = MagicMock()
        mock_instance.id = instance_id
        mock_instance.city_id = "0001"
        mock_instance.user_id = "0001"
        mock_instance.name = "My little house"
        mock_instance.number_rooms = 4
        mock_instance.number_bathrooms = 2
        mock_instance.max_guests = 10
        mock_instance.price_by_night = 300
        mock_instance.latitude = 37.773972
        mock_instance.longitude = 122.431297

        with patch('models.storage.all',
                   return_value={f"Place.{instance_id}": mock_instance}):
            instance = storage.all()[f"Place.{instance_id}"]
            self.assertEqual(instance.city_id, "0001")
            self.assertEqual(instance.user_id, "0001")
            self.assertEqual(instance.name, "My little house")
            self.assertEqual(instance.number_rooms, 4)
            self.assertEqual(instance.number_bathrooms, 2)
            self.assertEqual(instance.max_guests, 10)
            self.assertEqual(instance.price_by_night, 300)
            self.assertEqual(instance.latitude, 37.773972)
            self.assertEqual(instance.longitude, 122.431297)

    def test_create_with_invalid_params(self):
        """Test creating an object with invalid parameters"""

        class_name = "State"
        params = 'name="California" invalid_param=False'
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.console.do_create(f"{class_name} {params}")
            output = mock_stdout.getvalue().strip()
            # Check that an ID was printed
            self.assertTrue(len(output) > 0)

        instance_id = output
        mock_instance = MagicMock()
        mock_instance.id = instance_id
        mock_instance.name = "California"
        with patch('models.storage.all',
                   return_value={f"State.{instance_id}": mock_instance}):
            instance = storage.all()[f"State.{instance_id}"]
            self.assertEqual(instance.name, "California")
            self.assertFalse(hasattr(instance, "invalid_param"))


if __name__ == "__main__":
    unittest.main()

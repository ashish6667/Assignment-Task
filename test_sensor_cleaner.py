"""
Unit tests for sensor_cleaner.py
"""

import unittest
from sensor_cleaner import clean_and_normalize_sensor_readings


class TestSensorCleaner(unittest.TestCase):

    def test_valid_numbers_and_strings(self):
        # Checks converting integers, floats, and numeric strings
        input_data = [10, 20.5, "30.2", "100"]
        expected_output = [10.0, 20.5, 30.2, 100.0]
        self.assertEqual(clean_and_normalize_sensor_readings(input_data), expected_output)

    def test_negative_values_dropped(self):
        # Checks that negative values and error flags are filtered out
        input_data = [-1, -99.9, 0.0, 50.0]
        expected_output = [0.0, 50.0]
        self.assertEqual(clean_and_normalize_sensor_readings(input_data), expected_output)

    def test_none_and_invalid_strings_dropped(self):
        # Checks dropping None and non-numeric strings
        input_data = [None, "error", 22.4, None, "test"]
        expected_output = [22.4]
        self.assertEqual(clean_and_normalize_sensor_readings(input_data), expected_output)

    def test_clipping_above_500(self):
        # Checks capping numbers above 500.0
        input_data = [450.0, 500.0, 505.0, 999.0]
        expected_output = [450.0, 500.0, 500.0, 500.0]
        self.assertEqual(clean_and_normalize_sensor_readings(input_data), expected_output)

    def test_empty_and_invalid_lists(self):
        # Checks empty list and all-invalid inputs return []
        self.assertEqual(clean_and_normalize_sensor_readings([]), [])
        self.assertEqual(clean_and_normalize_sensor_readings([None, "bad", -5]), [])
        self.assertEqual(clean_and_normalize_sensor_readings(None), [])


if __name__ == "__main__":
    unittest.main()

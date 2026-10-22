"""
Section 1: Coding Logic & Sanitization
Clean and Normalize Sensor Readings
"""

def clean_and_normalize_sensor_readings(sensor_values):
    """
    Cleans a list of mixed sensor readings:
    1. Converts elements to float where possible. Drops unconvertible values, None, and negative (< 0) values.
    2. Clips numbers exceeding 500.0 to 500.0.
    3. Handles empty lists or invalid lists safely.
    """
    # Handle empty input or non-list inputs safely
    if not sensor_values or not isinstance(sensor_values, list):
        return []

    cleaned_values = []

    for item in sensor_values:
        # Skip None values
        if item is None:
            continue

        # In Python, bool is a subclass of int (True=1, False=0), so ignore booleans
        if isinstance(item, bool):
            continue

        # Try to convert element to float
        try:
            val = float(item)
        except (ValueError, TypeError):
            # Drop strings or items that cannot be converted to float
            continue

        # Drop negative error flags (< 0)
        if val < 0:
            continue

        # Clip values greater than 500.0 to 500.0
        if val > 500.0:
            val = 500.0

        cleaned_values.append(val)

    return cleaned_values


if __name__ == "__main__":
    print("Running Sensor Cleaner Tests...\n")

    # Test Case 1: Mixed inputs (valid floats, strings, None, negative numbers, invalid strings)
    test_1 = [12.5, "45.0", None, -5, "sensor_error", 550.0, 0]
    result_1 = clean_and_normalize_sensor_readings(test_1)
    print("Test Case 1:")
    print("Input: ", test_1)
    print("Output:", result_1)
    assert result_1 == [12.5, 45.0, 500.0, 0.0]

    # Test Case 2: Clipping values exceeding 500.0
    test_2 = [500.0, 501.2, 1000.0, 250.5]
    result_2 = clean_and_normalize_sensor_readings(test_2)
    print("\nTest Case 2 (Clipping):")
    print("Input: ", test_2)
    print("Output:", result_2)
    assert result_2 == [500.0, 500.0, 500.0, 250.5]

    # Test Case 3: Edge cases (empty list and all invalid entries)
    test_empty = []
    test_invalid = [None, "error", -10, "N/A", -999.0]
    print("\nTest Case 3 (Edge Cases):")
    print("Empty list output:      ", clean_and_normalize_sensor_readings(test_empty))
    print("All invalid list output:", clean_and_normalize_sensor_readings(test_invalid))
    assert clean_and_normalize_sensor_readings(test_empty) == []
    assert clean_and_normalize_sensor_readings(test_invalid) == []

    print("\nAll tests passed successfully!")

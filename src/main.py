"""
main.py
=======

Description:
------------
This is the entry point of the application, which demonstrates setting and retrieving values using keyring storage.
"""

from src.keyring_storage import get_value, set_value, set_and_retrieve_value_with_specific_backend


def main():
    """This method is the entry point of the application."""
    TEST_KEY = "test_key"
    TEST_KEY_WITH_SPECIFIC_BACKEND = "test_key_with_specific_backend"
    test_value = "Hello, I am keyring test value"
    test_value_with_specific_backend = "Hello, I am keyring test value with specific backend"
    
    # Set and retrieve value without specific backend
    print("\n--- Setting and Retrieving Value Without Specific Backend ---")
    set_value(TEST_KEY, test_value)
    print("Value retrieved for key '{}':".format(TEST_KEY), get_value(TEST_KEY))

    # Add extra line for separation
    print("\n--- Setting and Retrieving Value With Specific Backend ---")
    # Set and retrieve value with specific backend
    set_and_retrieve_value_with_specific_backend(TEST_KEY_WITH_SPECIFIC_BACKEND, test_value_with_specific_backend)
    

if __name__ == '__main__':
    main()

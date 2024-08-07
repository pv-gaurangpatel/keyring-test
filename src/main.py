"""
main.py
=======

Description:
------------
This is the entry point of the application.
"""

from src.keyring_storage import get_value, set_value


def main():
    """This method is the entry point of the application."""
    TEST_KEY = "test_key"
    test_value = "Hello i am keyring test value"
    
    set_value(TEST_KEY,test_value)

    print(get_value(TEST_KEY))


if __name__ == '__main__':
    main()

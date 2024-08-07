"""
This module contains the keyring class, which represents
an operation manager for keyring functionalities.
"""

import keyring as kr

APP_NAME = 'Keyring-test'

def set_value(key: str, value: str) -> None:
    """Set a value in the keyring with a specific key.

    Args:
        key: The key under which the value is stored.
        value: The value to store.
    """
    try:
        kr.set_password(APP_NAME, key, value)
        print('Password set successfully for key:', key)
    except kr.errors.KeyringError as error:
        print('Error setting password for key:', key)
        print('Error:', error)
    except Exception as error:
        print('Error:', error)
        return error  


def get_value(key: str):
    """Get a value from the keyring based on the key.

    Args:
        key: The key for which to retrieve the value.

    Returns:
        The retrieved value or None if an error occurred.
    """
    try:
        return kr.get_password(APP_NAME, key)
    except kr.errors.KeyringError as error:
        print('Error retrieving password for key:', key)
        print('Error:', error)
        return error
    except Exception as error:
        print('Error:', error)
        return error  


def delete_value(key: str) -> None:
    """Delete a value in the keyring associated with a specific key.

    Args:
        key: The key for which the value should be deleted.
    """
    try:
        kr.delete_password(APP_NAME, key)
        print('Password deleted successfully for key:', key)
    except kr.errors.KeyringError as error:
        print('Error deleting password for key:', key)
        print('Error:', error)


get_value(APP_NAME)

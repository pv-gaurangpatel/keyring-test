"""
This module contains the keyring class, which represents
an operation manager for keyring functionalities.
"""

import keyring as kr
from keyring.backends import SecretService

APP_NAME = 'Keyring-test'

def set_value(key: str, value: str) -> None:
    """Set a value in the keyring with a specific key.

    Args:
        key: The key under which the value is stored.
        value: The value to store.
    """
    try:
        backend = kr.get_keyring()
        print(f"Using backend: {backend}")
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
        backend = kr.get_keyring()
        print(f"Using backend: {backend}")
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


def set_and_retrieve_value_with_specific_backend(key: str, value: str) -> None:
    """Set a value in the keyring using a specific backend and handle exceptions.

    Args:
        key: The key under which the value is stored.
        value: The value to store.
    """
    try:
        # Set the specific backend
        backend = SecretService.Keyring()
        kr.set_keyring(backend)
        
        currnet_backend = kr.get_keyring()
        print(f"Current backend: {currnet_backend}")
        # Store the password using the chosen backend
        kr.set_password(APP_NAME, key, value)
        print(f"'set_and_retrieve_value_with_specific_backend'--> Password set successfully for key: {key}")

        # Retrieve the password to confirm it was set correctly
        
        password = kr.get_password(APP_NAME, key)
        if password is None:
            print(f"'set_and_retrieve_value_with_specific_backend'--> No password found for key: {key}")
        else:
            print(f"'set_and_retrieve_value_with_specific_backend'--> Retrieved password: {password}")
    
    except kr.errors.KeyringError as error:
        # Handle keyring-related errors
        print(f"'set_and_retrieve_value_with_specific_backend'--> Keyring error occurred while setting or retrieving password: {error}")
    
    except Exception as e:
        # Handle other unexpected errors
        print(f"'set_and_retrieve_value_with_specific_backend'--> An unexpected error occurred: {e}")

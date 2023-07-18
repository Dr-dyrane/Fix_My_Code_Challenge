#!/usr/bin/env python3

"""
User Password

This script defines a User class that represents a user and provides a method for validating passwords.

Requirements:
- Python 3

Usage:
  ./3-user.py

Example:
  user = User("Test User", "correctpassword")
  print(user.username)
  print(user.is_valid_password("correctpassword"))  # Output: True

Author:
- Alexander Udeogaranya
"""


class User:
    """
    User class represents a user.
    """

    def __init__(self, username, password):
        """
        Initialize a new User instance.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            None
        """
        self.username = username
        self.password = password

    def is_valid_password(self, input_password):
        """
        Check if the provided password matches the user's password.

        Args:
            input_password (str): The password to be checked.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        return input_password == self.password


if __name__ == "__main__":
    # Example usage
    user = User("Test User", "correctpassword")
    print(user.username)
    print(user.is_valid_password("correctpassword"))

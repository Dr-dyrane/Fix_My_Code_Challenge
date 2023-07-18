#!/usr/bin/env python3

"""
FizzBuzz

This script prints the numbers from 1 to n. For multiples of 3,
it prints "Fizz" instead of the number. For multiples of 5,
it prints "Buzz" instead of the number. For numbers that are
multiples of both 3 and 5, it prints "FizzBuzz".

Requirements:
- Python 3

Usage:
  ./fizzbuzz.py <n>

Example:
  ./fizzbuzz.py 50
  Output:
  1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz 16 17 Fizz 19 Buzz Fizz
  22 23 Fizz Buzz 26 Fizz 28 29 Fizz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41
  Fizz 43 44 Fizz 46 47 Fizz 49 Buzz

Author:
- Alexander Udeogaranya
"""


def fizzbuzz(n):
    """
    Prints the numbers from 1 to n following the FizzBuzz rules.

    Args:
        n (int): The maximum number to print.

    Returns:
        None
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()


if __name__ == "__main__":
    fizzbuzz(50)

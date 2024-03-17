#!/usr/bin/python3
"""
FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    -For multiple of three print "Fizz" instead ofthe nummber and for
    the multiple of fiv print "Buzz".
    -For numbers which are multiples of both three and five print "FizzBuZZ".
    """
    if n < 1:
        return

    for i in range(1, n + 1):
        if (i % 5) == 0 and (i % 3) == 0:
            print("FizzBuzz", end=" ")
        elif (i % 3) == 0:
            print("Fizz", end=" ")
        elif (i % 5) == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

number = int(sys.argv[1])
fizzbuzz(number)

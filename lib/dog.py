#!/usr/bin/env python3
class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

fida = Dog("Fida", "Mutta")
fida.breed = "Mutt"

print(fida.name)
print(fida.breed)


# A parity bit, or check bit, is a bit added to a string of bits to ensure that the total number of 1-bits in the string is even or odd. Parity bits are used as the simplest form of error detecting code.

# You have two parameters, one being the wanted parity (always 'even' or 'odd'), and the other being the binary representation of the number you want to check.

# Your task is to return an integer (0 or 1), whose parity bit you need to add to the binary representation so that the parity of the resulting string is as expected.

# Example:

#   Parity: 'even'
#   Bin: '0101010'
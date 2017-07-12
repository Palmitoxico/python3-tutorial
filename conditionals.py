#! /usr/bin/env python3

#
# Use and syntax of conditionals
#

a = 12

if a != 15:
    print("a is different from 15")

if a > 10:
    print("a is greater than 10")
else:
    print("a is lesser or equal to 10")

if a >= 13:
    print("a is greater or equal to 13")
elif a == 12:
    print("a is equal to 12")
else:
    print("a is neither 12 nor greater or equal to 13")


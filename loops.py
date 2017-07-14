#! /usr/bin/env python3

#
# Use and syntax of loops
#

a = 0
while a < 4:
    print(str(a))
    a += 1

# or in a more elegant way:
for a in range(5):
    print(str(a))

# break and continue:
for a in range(12):
    if a % 3 == 0:
        continue
    print(str(a))
    if a == 10:
        break
    
    

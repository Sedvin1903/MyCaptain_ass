"""   Assignment 2.2 - 2 """

# Make for loop infinite 

# 1st way
from itertools import count 
for i in count(0):
  print("Success")

# 2nd way
def infinity():
    while True:
        yield
for _ in infinity():
    print("Success")

import itertools
import math

with open('input') as f:
    Rawinput = f.read().splitlines()

# Convert from string to integer - and sort it
Numbers = sorted([int(number) for number in Rawinput])

# What's the target value?
Target = 2020

for Pair in itertools.product(Numbers, repeat=2):
    
    # Is the sum of that pair equal to the target?
    if sum(Pair) == Target:
        print("Solution for part 1:")
        print(f"Winning pair: {Pair}")

        # What's the product of that pair?
        Produkt = math.prod(Pair)
        print(f"Product: {Produkt}")

        # One result is enough, so break out of the for loop
        break


### Part 2
print("\n")

for Triplet in itertools.product(Numbers, repeat=3):
    
    # Is the sum of that triplet equal to the targe?
    if sum(Triplet) == Target:
        print("Solution for part 2:")
        print(f"Winning triplet: {Triplet}")

        # What's the product of that triplet?
        Product = math.prod(Triplet)
        print(f"Product: {Product}")

        # One result is enough, so break out of the for loop
        break

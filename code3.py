# Simple code for understanding argparse module
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("First_argument", help="Give a 1st number", type=int)
parser.add_argument("Second_argument", help="Give a 2nd number", type=int)



args = parser.parse_args()
x = args.First_argument
y = args.Second_argument

g = x * y

print("given 1st argument:", x)
print("given 2nd argument:", y)
print("Sum:", g)


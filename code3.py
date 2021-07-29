# Simple code for understanding argparse module:
# Run:python code3.py first_argument second_argument
# Import the required packages
import argparse
# create the ArgumentParser object
# The created object 'parser' will have the necessary information
# to parse the command-line arguments into data types.
parser = argparse.ArgumentParser()
# We add a positional argument using add_argument() including a help
parser.add_argument("First_argument", help="Give a 1st number", type=int)
parser.add_argument("Second_argument", help="Give a 2nd number", type=int)
# The information about program arguments is stored in 'parser'
# Then, it is used when the parser calls parse_args().
# ArgumentParser parses arguments through the parse_args() method:
args = parser.parse_args()
x = args.First_argument
y = args.Second_argument
g = x * y
# We get and print the first argument of this script:
print("given 1st argument:", x)
print("given 2nd argument:", y)
print("Sum:", g)


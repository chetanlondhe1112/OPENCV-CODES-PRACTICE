# use of vars() function dictionary
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

print("args: '{}'".format(args))
print("Sum:'{}'".format(args.First_argument + args.Second_argument))
# Additionally, the arguments can be stored in a dictionary calling vars() function:
args_dict = vars(parser.parse_args())
# printing of stored argument dictionary
print("args_dictionary:'{}'".format(args_dict))


# OUTPUT:
# E:\learning\open cv\Opencv-CODES-Practice>python code4.py 9 9
# args: 'Namespace(First_argument=9, Second_argument=9)'
# Sum:'18'
# args_dictionary:'{'First_argument': 9, 'Second_argument': 9}'





"""
Create a new python file.
● Set up argparse to take in a number from the command line. This can either be with a
flag or with positional arguments.
● You’ll be going from 0 to the number given on the command line.
● Set up your logger
● Info log the number that you’ve received from the arguments in argparse(The number to
send to the function).
● Pass the number into the function that you’ve written.
● Optional: Make the function recursive!
● Use the logger to output the sum to the user!
"""

import logging
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number", help="This is going to be the number added")


args = parser.parse_args()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logging.info(" Number Recieved: " + (args.number))


def sum(n:int) -> int:
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
    

print("The sigma addition is below:")
logging.warning(sum(int(args.number)))
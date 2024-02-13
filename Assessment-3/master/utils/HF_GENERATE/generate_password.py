import random
import string

def generate_password(digit):
    """
    Generates a random password consisting of uppercase letters and digits.

    Parameters:
    - digit (int): The length of the password to be generated.

    Returns:
    - str: A randomly generated password of the specified length.

    Dependencies:
    - string module: Required to access ASCII uppercase letters and digits.
    - random module: Required to generate random numbers for selecting characters.

    Example:
    >>> generate_password(8)
    '3S6R9T2U'
    >>> generate_password(12)
    '8Y2H6J1I7Z4K'
    """
    letter = string.ascii_uppercase + string.digits
    password = ''
    for digit in range(1,digit+1):
        password += letter[random.randint(0,len(letter)-1)]
    return password
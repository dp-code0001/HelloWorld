"""
    Similar to Two Fer example from Exercism.org
"""

name = input('Enter your name for a sulatation: ')

def test_repo(name):
    """
    Simple script to say Hello World as well as hello and goodbye to user.

    Args:
        param1: name string entered by user.

    Return:
        output phrase
    """
    # ternary expression that considers blank inputs and whitespace
    # inputs from the user, if they decide not to put in a name or string.
    name = 'you' if not name or name.isspace() else name
    return f'Hello, World! Hello to {name} as well! Goodbye!'

print(test_repo(name))

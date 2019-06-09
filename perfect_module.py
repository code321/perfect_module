#!/usr/bin/env python3.6.7
"""Add two digits and return result

Usage:
    python perfect_module.py <param1><param2>
    ./perfect_module.py <param1><param2>
    perfect_module.py <param1><param2>
    from perfect_module import add
    import perfect_module
    perfect_module.add(param1, param2)

"""

import sys

def add(a, b):
    """Add two digits and return result
    :param a: Digit as integer of float
    :param b: Digit as integer of float
    :return: A sum of two digits
    """
    return a  + b

if __name__=='__main__':
    try:
        print(add(sys.argv[1], sys.argv[2]))
    except Exception as error:
        print('Zle parametry')    
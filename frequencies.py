"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import numbers

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for key in items:
        if isinstance(key, numbers.Number): 
            key = str(key)
        if (key in frequencies): 
            frequencies[key] = frequencies[key] + 1
        else :
            frequencies[key] = 1

    return frequencies

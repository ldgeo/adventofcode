"""
answer part1 : 25190263477788
"""
import operator
import re

ops = {
    '+': operator.add,
    '*': operator.mul
}

pattern = re.compile(r'\(([\d\s\+\*]+)\)')


def reduce(it, initializer=None):
    """Custom reduce fuction handling 3 terms
    """
    if initializer:
        value = initializer
    else:
        value = next(it)
    try:
        op, d = next(it), next(it)
        yield from reduce(it, op(value, d))
    except StopIteration:
        yield value


def expr_to_list(expr):
    """replace operators with their corresponding functions
    """
    return [
        ops[elem] if elem in ('+', '*') else int(elem)
        for elem in re.split(r'(\+|\*)', expr)
    ]


def deep_compute(input):
    """Compute all sub groups of parenthesis, recursively
    """
    while match := pattern.search(input):
        input = input.replace(
            match.group(0),
            str(list(reduce(iter(expr_to_list(match.group(1)))))[0])
        )
    return input


with open('day18.input') as f:
    inputs = f.readlines()


print(sum(
    next(reduce(iter(expr_to_list(deep_compute(input)))))
    for input in inputs
))

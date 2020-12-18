"""
answer part1 : 25190263477788
answer part2 : 297139939002972

times:

python3.9: part1: 0.37s
python3.9: part2: 0.58s
"""
import operator
import re

ops = {
    '+': operator.add,
    '*': operator.mul
}

pattern = re.compile(r'\(([\d\s\+\*]+)\)')

# precedence_op = None
# part 2
precedence_op = re.compile(r'(\d+\s+\+\s+\d+)')


def reduce(it, initializer=None):
    """Recursive reduce with 3 terms
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
    """Replace operators with their corresponding functions
    """
    return [
        ops[elem] if elem in ('+', '*') else int(elem)
        for elem in re.split(r'(\+|\*)', expr)
    ]


def proxy_pred(input):
    """Proxy for precedence computation
    """
    if precedence_op:
        while pmatch := precedence_op.search(input):
            found = pmatch.group(1)
            input = input.replace(
                found,
                str(list(reduce(iter(expr_to_list(found))))[0])
            )
    return str(list(reduce(iter(expr_to_list(input))))[0])


def deep_compute(input):
    """Compute all sub groups of parenthesis
    """
    while match := pattern.search(input):
        input = input.replace(
            match.group(0),
            proxy_pred(match.group(1))
        )

    return input


with open('day18.input') as f:
    inputs = f.readlines()

print(sum(
    int(proxy_pred(deep_compute(input)))
    for input in inputs
))

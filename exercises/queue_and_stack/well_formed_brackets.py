"""
Test for well-formedness: EPI 8.3
"""


def is_well_formed(string):
    close_to_open = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    stack = []

    for bracket in string:
        if bracket not in close_to_open:
            stack.append(bracket)
        else:
            if not len(stack):
                return False
            opening_bracket = stack.pop()
            if close_to_open[bracket] != opening_bracket:
                return False

    if len(stack):
        return False

    return True


assert(is_well_formed('[[((({{{}}})))]]')) is True
assert(is_well_formed('(){}[](()){}{}')) is True
assert(is_well_formed('(){}(){}]')) is False
assert(is_well_formed('[(){}(){}')) is False

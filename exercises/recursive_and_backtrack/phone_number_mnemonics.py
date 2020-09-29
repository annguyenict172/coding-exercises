"""
Compute all mnemonics for a phone number: EPI 15.2
"""

def phone_number_mnemonics(phone_number):
    results = []
    backtrack(phone_number, 0, [], results)
    return results


def backtrack(phone_number, step, sequences, results):
    if step == len(phone_number):
        results.append("".join(sequences))
        return
    
    for char in number_to_chars[phone_number[step]]:
        sequences.append(char)
        backtrack(phone_number, step+1, sequences, results)
        sequences.pop()

number_to_chars = {
    '0': [],
    '1': [],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
}


print(phone_number_mnemonics('2276696'))

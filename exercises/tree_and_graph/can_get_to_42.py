"""
Alice has invented a new card game to play with Bob. Alice made a deck of cards with random values between 1 and 52.
Bob picks 5 cards. Then, he has to rearrange the cards so that by utilizing the operations plus, minus, or times, the
value of the cards reach Alice's favorite number, 42. More precisely, find operations such that
((((val1 op1 val2) op2 val3) op3 val4) op4 val5) = 42.

Help Bob by writing a program to determine whether it is possible to reach 42 given 5 card values.

For example, Bob picks 5 cards out of the deck containing 40, 1, 3, 4, and 20. Bob rearranges the cards and supplies
four operations, so that 4 * 20 - 40 + 3 - 1 = 42
"""
from copy import deepcopy
import unittest


class SearchNode:
    def __init__(self, target, available_nums, operator, chosen_num, previous):
        self.target = target
        self.available_nums = available_nums
        self.operator = operator
        self.chosen_num = chosen_num
        self.previous = previous


# As in the example, we have five cards: 40, 1, 3, 4, 20
# Recursively we can break down the problem like this:
# Is there any way to reach 42 + 20 or 42 - 20 or 42 / 20 with 40, 1, 3 and 4?
def can_get_to_42(num_list):
    solution_exists = False
    root = SearchNode(42, num_list, None, None, None)
    stack = [root]
    current_node = None

    # DFS to search for the solution
    while len(stack) > 0:
        current_node = stack.pop()
        if len(current_node.available_nums) > 1:
            for num in current_node.available_nums:
                # Try four operators to see if we can reach the new target from the remaining numbers
                list_without_num = deepcopy(current_node.available_nums)
                list_without_num.remove(num)

                if current_node.target % num == 0:
                    stack.append(
                        SearchNode(current_node.target / num, list_without_num, '/', num, current_node)
                    )

                stack.append(
                    SearchNode(current_node.target + num, list_without_num, '+', num, current_node)
                )
                stack.append(
                    SearchNode(current_node.target - num, list_without_num, '-', num, current_node)
                )
        else:
            # If the last number is equal to the target, that means we have found a solution
            if current_node.target == current_node.available_nums[0]:
                solution_exists = True
                break

    # This part is optional (to get the steps)
    if solution_exists:
        # Trace back to get the step
        reverse_operator = {
            '-': '+',
            '+': '-',
            '/': '*'
        }
        steps = [str(int(current_node.target))]
        while current_node.previous is not None:
            steps.append(reverse_operator[current_node.operator])
            steps.append(str(current_node.chosen_num))
            current_node = current_node.previous
        print('How to get to 42:')
        print(' '.join(steps))

    return solution_exists


class TestResult(unittest.TestCase):

    def test_solution_exists_with_40_1_3_4_20(self):
        self.assertTrue(can_get_to_42([40, 1, 3, 4, 20]))


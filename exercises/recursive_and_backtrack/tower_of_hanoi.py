"""
Tower Of Hanoi: EPI 15.1
"""


def print_move(disk, fr, to):
    print('Move disk {} from {} to {}'.format(disk, fr, to))


def tower_of_hanoi(disk, fr, to, spare):
    if disk == 1:
        print_move(disk, fr, to)
    else:
        tower_of_hanoi(disk - 1, fr, spare, to)
        print_move(disk, fr, to)
        tower_of_hanoi(disk - 1, spare, to, fr)


tower_of_hanoi(3, 'A', 'C', 'B')

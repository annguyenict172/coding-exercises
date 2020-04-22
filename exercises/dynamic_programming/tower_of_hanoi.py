"""
Tower of Hanoi
"""


def tower_of_hanoi(n):
    return move_tower(n, 'A', 'C', 'B')


def move_tower(disk, source, dest, spare):
    if disk == 1:
        print('Move disk 1 from {} to {}'.format(source, dest))
        return
    else:
        move_tower(disk-1, source, spare, dest)
        print('Move disk {} from {} to {}'.format(disk, source, dest))
        move_tower(disk-1, spare, dest, source)


tower_of_hanoi(3)

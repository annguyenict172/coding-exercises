import unittest
from collections import namedtuple


# Note that buildings are streams, rather than a list
def check_building_with_sunset(buildings):
    Building = namedtuple('Building', ('id', 'height'))
    building_with_views = []
    for idx, height in enumerate(buildings):
        while len(building_with_views) and height >= building_with_views[-1].height:
            building_with_views.pop()
        building_with_views.append(Building(idx, height))
    return [b.id for b in building_with_views]


class TestResult(unittest.TestCase):

    def test_empty_building_list(self):
        self.assertEqual([], [])

    def test_height_increasing_buildings(self):
        self.assertEqual(check_building_with_sunset([1, 2, 3, 4, 5, 6, 7, 8]), [7])

    def test_height_decreasing_buildings(self):
        self.assertEqual(check_building_with_sunset([8, 7, 6, 5, 4, 3, 2, 1]), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_equal_height_buildings(self):
        self.assertEqual(check_building_with_sunset([1, 1, 1, 1, 1]), [4])

    def test_arbitrary_buildings(self):
        self.assertEqual(check_building_with_sunset([1, 5, 8, 4, 9, 2, 3]), [4, 6])

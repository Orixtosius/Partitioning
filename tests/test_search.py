# -*- coding: utf-8 -*-

from context import partition
from partition.search import SubsetSearcher
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.searcher = SubsetSearcher()
        self.main_set = [8, 7, 6, 5, 4]

    def test_equal_partition(self):
        subset_1, subset_2, difference = self.searcher.execute(self.main_set, 2)
        self.assertEqual(difference, 0)
        self.assertEqual(subset_1, [6, 5, 4])
        self.assertEqual(subset_2, [8, 7])

    def test_equal_partition_2(self):
        subset_1, subset_2 = self.searcher.execute_diff(self.main_set, 2)
        #self.assertEqual(subset_1, [7, 5, 4])
        self.assertEqual(subset_2, [8, 6])

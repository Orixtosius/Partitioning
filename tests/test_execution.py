# -*- coding: utf-8 -*-

#from .context import partition
from partition.core import Partition
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.partitioner = Partition()
        self.main_set = [2, 2, 3, 4, 5, 6]
        return super().setUp()

    def test_equal_partition(self):
        self.partitioner.execute(self.main_set, 2)

        temp_sum = sum(self.partitioner.subsets[0])
        for subsets in self.partitioner.subsets[1:-1]:
            subset_sum = sum(subsets)
            self.assertEqual(temp_sum, subset_sum)
            temp_sum = subset_sum

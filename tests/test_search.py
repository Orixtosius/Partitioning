# -*- coding: utf-8 -*-

from context import core
from core.search.cumulative_search import CumulativeSearcher
from core.execution import Executor
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.executor = Executor()
        self.main_set = [8, 7, 6, 5, 4]

    def test_equal_partition(self):
        subset_1, subset_2 = self.executor.execute_cumu(self.main_set, 2)
        self.assertCountEqual(subset_1, [6, 5, 4])
        self.assertCountEqual(subset_2, [8, 7])

    def test_equal_partition_2(self):
        subset_1, subset_2 = self.executor.execute_diff(self.main_set, 2)
        self.assertCountEqual(subset_1, [7, 5, 4])
        self.assertCountEqual(subset_2, [8, 6])

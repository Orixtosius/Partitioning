from core.search.differenciative_search import DifferenciativeSearcher
from core.search.cumulative_search import CumulativeSearcher


class Executor:

    def __init__(self):
        self.diff_searcher = DifferenciativeSearcher()
        self.cumu_searcher = CumulativeSearcher()

    def assign_for_process(self, items: list[int], subset_number: int):
        self.items = items
        self.subset_number = subset_number
        self.target = sum(self.items) // self.subset_number

    def sort_before_returning(self, *subsets):
        sorted_subsets = [sorted(s, reverse=True) for s in subsets]
        return sorted_subsets

    def execute_diff(self, items: list[int], subset_number: int) -> list:

        self.assign_for_process(items, subset_number)
        primary_subset, secondary_subset = self.diff_searcher.search(items)
        sorted_primary_subset, sorted_secondary_subset = self.sort_before_returning(primary_subset, secondary_subset)

        return sorted_primary_subset, sorted_secondary_subset
    
    def execute_cumu(self, items: list[int], subset_number: int) -> list:

        self.assign_for_process(items, subset_number)
        primary_subset, secondary_subset = self.cumu_searcher.search(items, list())

        return primary_subset, secondary_subset
from ..partition import Partitioner
from search_interface import Search

class CumulativeSearcher(Search):

    def search(self, cumulative_subset: list[int], remaining_subset: list[int]) -> tuple[list[int], list[int]]:
        
        # If subset has a largest number that more than sum of rest
        if cumulative_subset[0] >= sum(cumulative_subset[1:]):
            return cumulative_subset[1:], remaining_subset

        updated_subsets = self.partitioner.partition_with_sum(cumulative_subset, remaining_subset)
        return self.search(*updated_subsets)
      
    # def execute_diff(self, items: list[int], subset_number: int):
    #     self.items = items
    #     self.partitioner = Partitioner()
    #     self.subset_number = subset_number
    #     self.target = sum(self.items) // self.subset_number

    #     subsets = self.search_diff(items)
    #     return subsets
    
    # def execute(self, items: list[int], subset_number: int):
    #     self.items = items
    #     self.partitioner = Partitioner()
    #     self.subset_number = subset_number
    #     self.target = sum(self.items) // self.subset_number

    #     primary_subset, secondary_subset = self.search(items, list())
    #     difference = self.calculate_discrepancy(primary_subset, secondary_subset)

    #     return primary_subset, secondary_subset, difference

    def set_subset_number(self, subset_number: int):
        if subset_number < 2:
            raise ValueError
        elif subset_number > 2:
            raise ValueError
        self.subset_number = subset_number

    @staticmethod
    def has_items_in_subset(subset: list[int]):
        return (len(subset) > 0)
    
    @staticmethod
    def has_largest_number_less_than_sum_of_rest(subset: list[int]):
        largest_number = subset[0]
        return (largest_number < subset[1:])
    
    def has_subset_sum_reached_target(self, subset: list[int]):
        return (sum(subset) == self.target)
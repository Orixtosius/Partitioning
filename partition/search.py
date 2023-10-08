from .partition import Partitioner

class SubsetSearcher:

    def search(self, cumulative_subset: list[int], remaining_subset: list[int]) -> tuple[list[int], list[int]]:
        
        # If subset has a largest number that more than sum of rest
        if cumulative_subset[0] >= sum(cumulative_subset[1:]):
            return cumulative_subset[1:], remaining_subset

        updated_subsets = self.partitioner.partition_with_sum(cumulative_subset, remaining_subset)
        return self.search(*updated_subsets)
    
    def search_diff(self, subset):
        if len(subset) == 2:
            if subset[0] > subset[1]:
                return [subset[0]], [subset[1]]
            return [subset[1]], [subset[0]]

        largest = subset[0]
        second_largest = subset[1]
        
        updated_subsets = self.partitioner.partition_with_differenciating(subset)
        subsets = self.search_diff(updated_subsets)

        rearranged_updated_subset = self.rearrange_subset(subsets, largest, second_largest)

        return rearranged_updated_subset
    
    def rearrange_subset(self, subsets: list[list[int]], largest_number: int, second_largest_number: int) -> list[list[int]]:
        searched_number = largest_number - second_largest_number
        for s in subsets:
            if searched_number in s:
                s.remove(searched_number)
                s.append(largest_number)             
            else:
                s.append(second_largest_number)
            sorted(s, reverse=True)
        return subsets

    def execute_diff(self, items: list[int], subset_number: int):
        self.items = items
        self.partitioner = Partitioner()
        self.subset_number = subset_number
        self.target = sum(self.items) // self.subset_number

        subsets = self.search_diff(items)
        return subsets

    def calculate_discrepancy(self, subset_1, subset_2):
        return sum(subset_1) - sum(subset_2)
    
    def execute(self, items: list[int], subset_number: int):
        self.items = items
        self.partitioner = Partitioner()
        self.subset_number = subset_number
        self.target = sum(self.items) // self.subset_number

        primary_subset, secondary_subset = self.search(items, list())
        difference = self.calculate_discrepancy(primary_subset, secondary_subset)

        return primary_subset, secondary_subset, difference

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


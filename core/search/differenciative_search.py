from core.search.search_interface import Search


class DifferenciativeSearcher(Search):

    def search(self, subset):
        if len(subset) == 2:
            if subset[0] > subset[1]:
                return [subset[0]], [subset[1]]
            return [subset[1]], [subset[0]]

        largest = subset[0]
        second_largest = subset[1]
        
        updated_subsets = self.partitioner.partition_with_differenciating(subset)
        subsets = self.search(updated_subsets)

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
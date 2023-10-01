class Partitioner:
  
    def partition_with_sum(self, cumulative_subset, remaining_subset) -> list[list[int]]:
        """"""    
        largest_number = cumulative_subset[0]
        second_largest_number = cumulative_subset[1]

        remaining_subset.extend([largest_number, second_largest_number])
        cumulative_subset.remove(second_largest_number)
        cumulative_subset[0] = largest_number + second_largest_number

        return cumulative_subset, remaining_subset
    
    def partition_with_differenciating(self, cumulative_subset, remaining_subset) -> list[list[int]]:
        """"""
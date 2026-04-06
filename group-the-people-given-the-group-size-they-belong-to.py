class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        
        groups_by_size = {}
        n = len(groupSizes)

        for i in range(n):
            size = groupSizes[i]
            if size not in groups_by_size:
                groups_by_size[size] = []
            groups_by_size[size].append(i)
        
        result = []
        for size, people_ids in groups_by_size.items():
            current_group_start = 0
            while current_group_start < len(people_ids):
                result.append(people_ids[current_group_start : current_group_start + size])
                current_group_start += size
                
        return result

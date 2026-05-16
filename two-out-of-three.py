class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq={}
        for num in set(nums1):
            freq[num]=freq.get(num,0)+1
        for num in set(nums2):
            freq[num]=freq.get(num,0)+1
        for num in set(nums3):
            freq[num]=freq.get(num,0)+1
        return [num for num,count in freq.items() if count>=2]
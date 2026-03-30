class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        low = 0
        high = n - 1
        
        ans = letters[0] 
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if letters[mid] > target:
                ans = letters[mid]
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
# class CustomFunction:
#    def f(self, x, y):
#        """
#        :type x: int
#        :type y: int
#        :rtype: int
#        """

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> list[list[int]]:
        results = []
        
        x = 1
        y = 1000 
        
        while x <= 1000 and y >= 1:
            current_f_val = customfunction.f(x, y)
            
            if current_f_val == z:
                results.append([x, y])
                x += 1
                y -= 1
            elif current_f_val < z:
                x += 1
            else:
                y -= 1
                
        return results

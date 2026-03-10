# """
# This is the interface for NestedInteger, which is already defined.
# You should not implement it, or speculate about its implementation.
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise, initializes a single integer.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            # If the string does not start with '[', it's a single integer.
            return NestedInteger(int(s))

        stack = []
        current_number_str = ""
        root_list = None # This will hold the outermost NestedInteger list

        for char in s:
            if char == '[':
                new_list = NestedInteger()
                if stack:
                    # If there's a parent list on the stack, add this new list to it.
                    stack[-1].add(new_list)
                else:
                    # If the stack is empty, this is the very first list being created,
                    # which means it's the root of our deserialized structure.
                    root_list = new_list
                stack.append(new_list)
            elif char == ']' or char == ',':
                if current_number_str:
                    # If we've accumulated digits (and possibly a leading minus sign),
                    # it means we've parsed an integer.
                    ni_int = NestedInteger(int(current_number_str))
                    # Add this integer to the list currently at the top of the stack.
                    stack[-1].add(ni_int)
                    # Reset the number string for the next integer.
                    current_number_str = ""
                if char == ']':
                    # If a ']' is encountered, the list at the top of the stack is complete.
                    # It has already been added to its parent (if any), so we pop it.
                    # The stack should not be empty here for a valid input string,
                    # as it always contains the current list being processed.
                    stack.pop()
            else: 
                # If char is a digit or '-', append it to the current number string.
                current_number_str += char
        
        # After processing all characters, root_list will contain the fully deserialized structure.
        return root_list

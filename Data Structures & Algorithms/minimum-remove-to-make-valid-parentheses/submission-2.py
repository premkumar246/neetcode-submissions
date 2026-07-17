# Data Structure: Strings
# Patterns: String fundamentals 
# Process:
# Traverse through the string 
# for every "(" charecter add the index of it to the list 
# every time ")" empty one charecter index in the list when the list is not empty
# when the list is empty add that index to a set
# after the traversal list has all the "(" indices where no match of ")" found
# the set has all the indices of ")" where no match of "(" found
# now add the stack to the set 
# create a new string by escaping the charecters of indices in the set and return the final string 
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()

        for i,v in enumerate(s):

            if v == "(":
                stack.append(i)

            elif v == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        while stack:
            remove.add(stack.pop())
        
        new_string = ""

        for i,v in enumerate(s):
            if i in remove:
                continue
            else:
                new_string+=v
        return new_string 
        
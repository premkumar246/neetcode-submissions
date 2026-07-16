# Data structure: Strings
# Pattern: String basics
# Type: stripping and split  
# Process:
# strip the string all ther empty spaces 
# split the string based on space
# read the last word and return the len of the word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last_word =s.split(" ")[-1]
        return len(last_word)
        
        
""" Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = 0
        lower = 0
        fupper = False
        l = len(word)
        for i in range(l):
            if word[i].isupper() == True:
                upper +=1
            if i == 0 and word[i].isupper() == True:
                fupper = True
            if word[i].islower() == True:
                lower +=1
        if upper == l:
            return True
        elif lower == l:
            return True
        elif fupper == True and lower == l - 1:
            return True
        else:
            return False

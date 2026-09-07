class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def count_letters(word):
            count = {}
            for letter in word:
                if letter in count:
                    count[letter] += 1
                else:
                    count[letter] = 1
            return(count)

        if count_letters(s) == count_letters(t):
            return True
        else:
            return False



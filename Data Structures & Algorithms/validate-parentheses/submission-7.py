class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        parenthesis_dict = {"(" : ")", "{" : "}", "[" : "]"}

        for char in s:
            if char in parenthesis_dict.keys():
                open_stack.append(char)
            if char in parenthesis_dict.values():
                try:
                    opener_parenthesis =  open_stack.pop()
                except:
                    return False
                if parenthesis_dict[opener_parenthesis] != char:
                    return False
                    
        return True if not open_stack else False
# balanced_parentheses.py

'''
Base idea for algorithm:
0 - Sanitize string
    - Assume that there can be spaces and whitespace, but nothing other than the testable characters
    - Remove all whitespace
1 - Declare stack (to store reference to the tokens being read)
2 - Loop through each char
    - Check
        - Is char valid?
        - Is char an endchar?
            - Check stack
                - If matches top of stack, remove top of stack
                - Else, the string isn't valid, return false
        - Is char a startchar?
            - Add to stack
3 - If loop ends:
        - Check stack size, if 0 return true,
        - Else, return false (open parentheses still left)

Sources:
https://bradfieldcs.com/algos/stacks/balanced-parentheses/
'''

class NotStringError(ValueError): pass
class NotParenthesisError(ValueError): pass

def is_balanced(str_):
    '''Determines whether the provided string is balanced or not'''

    token_dict = {')': '(', # defines the tokens to be ckecked and their opening counterparts
                  ']': '[',
                  '}': '{'}

    stack = [] # stores the open tokens while iterating through the string
    
    def sanitizer(str_):
        '''Returns a string without whitespaces'''
        return ''.join(str_.split())

    def check(chr_):
        '''Checks if the character is the start of a new block or the end of the latest block'''
       
        if chr_ in token_dict.values(): # start token
            stack.append(chr_)
            return True
        elif chr_ in token_dict.keys(): # end token
            try:
                if stack[-1] == token_dict.get(chr_): # endchr matches with the top of the stack, so the token block is closed, hence we try to close the next enclosing block
                    stack.pop()
                    return True
                else: # endchr doesn't match with the top of the stack, so the block is irregular
                    return False
            except IndexError: # tried to access an empty list
                return False
        else: # chr_ isn't included anywhere as a value or a key of the token_dict, so it's not a valid character
            raise NotParenthesisError('string contains non-parentheses character')

    if not isinstance(str_, str):
        raise NotStringError('input is not a string')

    str_ = sanitizer(str_)

    for chr_ in str_:
        if not check(chr_):
            return False
    
    if len(stack):
        return False # if the stack has at least one element, then there are still open parentheses, so the string isn't balanced
    else:
        return True  # if the stack is empty, everything has been balanced

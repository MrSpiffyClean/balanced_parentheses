# balanced_parentheses_generator.py
'''
Code for generating a random valid parenthesis string
'''

import random

def string_generator():
    '''Generates a string that will pass a balanced parentheses test
    Idea as follows:
    1 - Declare stack and return string
    2 - Randomly choose length of process
    3 - For each cycle of the process:
        - Choose a token to append to the return string
            - If stack is empty, any of the three starting tokens
            - If stack has a token, choose from the 3 plus the closing token matching the top of the stack
                - If matched token is chosen, pop top of stack
    4 - After the process has ended, unwind the stack:
        - Top to bottom, append to the return string the matching tokens
    5 - Return constructed string
    '''

    token_dict = {'(': ')',
                  '[': ']',
                  '{': '}'}

    stack = []
    str_ = ''

    for i in range(random.randrange(100)):
        if len(stack):
            chr_ = random.choice([*token_dict.keys(), token_dict.get(stack[-1])])
            str_ += chr_
            if chr_ == token_dict.get(stack[-1]):
                stack.pop()
            else:
                stack.append(chr_)
        else:
            chr_ = random.choice([*token_dict.keys()])
            str_ += chr_
            stack.append(chr_)

    for token in stack[::-1]:
        str_ += token_dict.get(token)

    return str_

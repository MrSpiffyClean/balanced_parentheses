# balanced_parentheses_test.py
import balanced_parentheses
import unittest

'''
Unit testing:

We have a function, is_balanced(), that takes a string as input and outputs True if it is balanced, 
False if it is not, ignoring whitespace, and raises an exception if it finds anything unexpected
(such as a character that isn't a parentheses)

Sources:
https://diveintopython3.net/unit-testing.html
https://docs.python.org/3/library/unittest.html
'''

class KnownValues(unittest.TestCase):
    known_values = (('', True), # assume that an empty string is balanced
                    ('()', True), # Standard 1-depth cases
                    ('[]', True),
                    ('{}', True),
                    ('(', False), # Single char cases
                    (']', False),
                    ('}', False),
                    (')', False),
                    (']', False),
                    ('}', False),
                    ('( )', True), # Testing whitespace
                    ('[  ]', True),
                    ('\n{ \t }\n', True),
                    ('   (', False),
                    (' ]   ', False),
                    ('  } 	', False),
                    ('(())', True), # 2-depth cases
                    ('[[]]', True),
                    ('{{}}', True),
                    ('([]{}[])', True),
                    ('[()]', True),
                    ('{{([])()}[][(({}[]))]}', True), # variable-depth
                    ('([)]', False),
                    ('{[}]', False),
                    ('{(})', False),
                    ('())))))', False), # Unbalanced constructs
                    ('[[[]', False),
                    ('{{{}}', False),
                    ('()()()(()()())', True), # Uncontained parentheses
                    ('()[]{}({[](){}})', True),
                    ('[]([()[]]{})', True),
                    ('{{([][])}()}', True), # Other examples
                    ('{[])', False),
                    ('((()))', True),
                    ('(()', False),
                    ('())', False),
                    ('{ () [()] }', True), # Email examples
                    ('[ [(]) { (]) }', False))
    
    def test_is_balanced_known_values(self):
        '''is_balanced should give known result with known input'''
        for str_, result in self.known_values:
            self.assertEqual(balanced_parentheses.is_balanced(str_), result)

class IsBalancedBadInput(unittest.TestCase):
    def test_non_string(self):
        '''is_balanced should fail if the input is not a string'''
        self.assertRaises(balanced_parentheses.NotStringError, balanced_parentheses.is_balanced, 123) # int
        self.assertRaises(balanced_parentheses.NotStringError, balanced_parentheses.is_balanced, 0.5) # float
        self.assertRaises(balanced_parentheses.NotStringError, balanced_parentheses.is_balanced, ['(', ')'])  # list with strings
        self.assertRaises(balanced_parentheses.NotStringError, balanced_parentheses.is_balanced, {'(':')', ')':'('}) # dict with strings

    def test_string_with_not_parentheses(self):
        '''is_balanced should fail if the string input contains non-parenthesis characters'''
        self.assertRaises(balanced_parentheses.NotParenthesisError, balanced_parentheses.is_balanced, '(a balanced string)')

if __name__ == '__main__':
    unittest.main()

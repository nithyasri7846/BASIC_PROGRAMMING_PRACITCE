'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to match closing to opening brackets
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Pop from stack if not empty, else use dummy value
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket
                stack.append(char)

        # If stack is empty at the end, it's valid
        return not stack

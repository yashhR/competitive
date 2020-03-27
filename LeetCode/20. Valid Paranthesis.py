'''
Classic Stack problem, you may have learned this in your DS class in 3rd semester, this is probably the only
application of stack that the curicculum designers could come up with lol


Create a dictionary with the compliments of all the paranthesis.
So, this is simple. For every char in the given string, you check if the char is in the compliments dictionary, if it is
1. push to the stack
if it is not, then it must be the closing paranthesis, so you check for the last entered element in the stack i.e, peek
if the both are compliments of each other, COOL, take it out and go on,
if they are NOT, red flag - fuck it! Not a valid paranthesis.
'''


def isValid(s: str) -> bool:
    compliment = {'(': ')', '{': '}', '[': ']'}
    mystack = []
    for i in range(len(s)):
        if s[i] in compliment:
            mystack.append(s[i])
        else:
            try:
                if compliment[mystack[-1]] == s[i]:
                    mystack.pop()
                else:
                    return False
            except IndexError as exception:
                return False
    if len(mystack) == 0:
        return True
    return False


print(isValid("{[(])}"))

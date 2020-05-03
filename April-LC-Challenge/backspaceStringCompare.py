'''
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
'''


def solution1(s, t):
    s = list(s)
    t = list(t)
    while True:
        changed = False
        for i in range(len(s)-1):
            if s[i+1] == '#':
                changed = True
                del s[i:i+2]
                break
        if not changed:
            break
    while True:
        changed = False
        for i in range(len(t) - 1):
            if t[i + 1] == '#':
                changed = True
                del t[i:i+2]
                break
        if not changed:
            break
    s1 = ''
    for c in s:
        if c != '#':
           s1 += c
    t1 = ''
    for c in t:
        if c != '#':
            t1 += c
    print(s1, t1)
    if s1 == t1:
        return True
    return False
# This solution beats 71% of all python submissions

print(solution1("y#fo##f", "y#f#o##f"))

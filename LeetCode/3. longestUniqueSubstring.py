#  Given a string, find the length of the longest substring without repeating characters and also return the string

def lengthOfLongestSubstring(s: str):
    seen = {}  # hash set to keep track of all the characters (NOT extra space because it doesn't scale with input)
    start = 0  # pointer to indicate the start of the new substring
    end = 0    # pointer to indicate the end of the new substring
    longest = 0   # return value that increases with increase in size of unqiue substring

    while end < len(s):
        if s[end] not in seen:
            seen[s[end]] = end
            end += 1
            if len(seen) > longest:
                longest = len(seen)
                substr = s[start: end]
        else:
            del seen[s[start]]
            start += 1
    return longest, substr


print(lengthOfLongestSubstring("pwwwkekp"))
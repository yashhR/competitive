'''
Well, this comes under the EASY CATEGORY in Leetcode. So, I could solve it in one go.
Initial thoughts:
    1. STRINGS ARE IMMUTABLE IN PYTHON, so you CAN'T MAKE CHANGES IN PLACE, need a list for it

So, split the string into a list and traverse through it
As you go through it, store the vowels you encouter along with their positions.

Now, all you have to do is one by one in the positions, insert the vowels in reverse order.
Literally doing what you were told to. So, I implemented it and I thought this would actually be a really bad solution.

Surprisingly, it did better than 57% of all solutions, so I thought why not better the solution by making some
changes in operations and storage.


-----------------------------------------------------------------------------------------------------------------------


Instead of mainting two seperate lists, use the enumerate funtion and store both the indices and vowels as a tuple.
-- We should swap the first vowel with the last vowel, second with last second, third with last third
-- In the above case, you only have to do that for the first half of the elements right, else if you do that with all
   the positions,  you are just reswapping the elements,
-- So, go through the half of the list that has the positions in them and swap the values in the last for the ith
    element with the n-1-i th element.
-- I thought this will do better than the 1st approach, But this ended up doing better than only 19% of all Py sols


------------------------------------------------------------------------------------------------------------------------

So, I peeked at the discussions tab and read the first line, "JAVA two-pointer solution"
So, I came back because I knew what to do.

1 -- Set two pointers, one at the front, one at the end.
2 -- Keep moving the pointers (both towards each other) and for each of the pointers, move until you find a vowel
3 -- As soon as you find the vowels at both ends, swap them.
4 -- Do this until the front pointer is less than the end pointer, because, as soon as the front pointer meets or
    passes through the end pointer, it means that we have looped through the list once and for all.
5 -- This is the best solution because WE ONLY HAVE TO LOOP THROUGH THE LIST ONCE.

Note: Two pointer solutions are the best!
'''


# def reverseVowels(s: str) -> str:
#     vowels = []
#     positions = []
#     all_chars = []
#     hehe = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
#     for i in range(len(s)):
#         if s[i] in hehe:
#             vowels.append(s[i])
#             positions.append(i)
#         all_chars.append(s[i])
#     n = len(vowels)
#     for i in range(len(positions)):
#         all_chars[positions[i]] = vowels[n-1-i]
#     return ''.join(all_chars)
#
#
# # This is faster than 56.6% of all python solutions
# print(reverseVowels("hello"))
#
#
# def reverse_vowels(s):
#     positions = []
#     vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
#     return_string = []
#     for each in enumerate(s):
#         if each[1] in vowels:
#             positions.append(each[0])
#         return_string.append(each[1])
#     n = len(positions)-1
#     for i in range(len(positions)//2):
#         return_string[positions[i]], return_string[positions[n-i]] = return_string[positions[n-i]],
#         return_string[positions[i]]
#     return ''.join(return_string)
#
#
# # This is faster than 31.91% of all python solutions
# print(reverse_vowels("Leetcode"))


# def reverse_vowels(s):
#     vowels, all_chars, count = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'), [], 0
#     for c in s:
#         if c in vowels:
#             count += 1
#         all_chars.append(c)
#     count, front, end = count//2, -1, len(s)
#     while front < end and count:
#         front += 1
#         end -= 1
#         # print(f"front: {front, all_chars[front]}, end = {end, all_chars[end]}")
#         while True:
#             if all_chars[front] in vowels:
#                 ff = True
#                 break
#             else:
#                 front += 1
#         # print(f"front: {front, all_chars[front]}, end = {end, all_chars[end]}")
#         while True:
#             if all_chars[end] in vowels:
#                 fe = True
#                 break
#             else:
#                 end -= 1
#         # print(f"front: {front, all_chars[front]}, end = {end, all_chars[end]}")
#         if ff and fe:
#             all_chars[front], all_chars[end] = all_chars[end], all_chars[front]
#             count -= 1
#         # print(all_chars)
#     return ''.join(all_chars)
#
#
# This is faster than 19.21% of all python solutions
# print(reverse_vowels("aA"))


# def reverse_vowels(s):
#     s = list(s)
#     vowels = set("aeiouAEIOU")
#     l, r = 0, len(s)-1
#     while l <= r:
#         while l <= r and s[l] not in vowels: l+=1
#         while l <= r and s[r] not in vowels: r-=1
#         if l > r: break
#         s[l], s[r] = s[r], s[l]
#         l += 1
#         r -= 1
#     return ''.join(s)
#
# This is faster than 83% of all python solutions
# print(reverse_vowels("Leetcode"))

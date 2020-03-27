# def strStr(haystack: str, needle: str) -> int:
#     haha = len(needle)
#     if haha == 0:
#         return 0
#     for i in range(len(haystack)):
#         if haystack[i: i + haha] == needle:
#             return i
#     return -1

def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    return haystack.index(needle)

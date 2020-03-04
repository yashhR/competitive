def strStr(A, B):
    bro = A.replace(B, '$', 1)
    if '$' in bro:
        return bro.index('$')
    else:
        return -1
print(strStr("strstr", "str1"))
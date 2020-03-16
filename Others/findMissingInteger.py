'''
Given two arrays, find the misssing only missing integer in the second array,
example:

a = [4, 9, 69, 12, 5]
b = [12, 69, 9, 4]

output: 5
'''

'''
------------------------------------------------------------------------------------------------------------------------
Naive approach:

1. You go through every element of the first list and check if it is in the second list and
    if it is NOT, we return that element as the missing element.

    The code for it would look like this:
'''


'''
def find_missing(list1, list2):
    for num1 in list1:
        flag = 0
        for num2 in list2:
            if num1 == num2:
                flag = 1
                break
            else:
                flag = 0
        if flag:
            print(f"{num1} is present")
        else:
            print(f"{num1} is the missing element")
            return num1


find_missing([4, 9, 12, 69, 5], [69, 12, 4, 9])


'''
'''
The above solution is the worst you could possibly do if given in an interview
This is plain brute-force, and you'd definitely NOT want to do this in an interview

Analysis:
    1. Time Complexity:
        For every element in list1, you are going through every element in list2, 
        so that becomes O(n^2)
    2. Space Complexity:
        You aren't taking any extra space, which is the only good thing about this approach

There's a more fancier way of doing this, in fact, a more pythonic way of doing this:
that is, by using the "in" operator. This is essentially the exact same approach but just less hard coded.

'''

'''
------------------------------------------------------------------------------------------------------------------------
def fancier_missing_element(list1, list2):
    for num1 in list1:
        if num1 not in list2:
            print(num1, "is the missing element")
            return num1


fancier_missing_element([4, 9, 12, 69, 5], [69, 4, 12, 9])
'''
'''
The "in" and "not in" operators are basically LOOK-UPS.
LOOK-UPs in lists is O(n) which again, makes the problem as a quadratic time complexity
which is PRETTY BAD for coding interviews
'''

'''
As we have observed, the problem is with the lookups in lists, if somehow we are able to lookup
into the second list in constant time, we will have a linear solution, which is good enough.

LOOK UP in O(1) time, what data structure does that? HASH tables
Khatham.
'''
'''
------------------------------------------------------------------------------------------------------------------------
def find_missing_using_ht(list1, list2):
    check = {}
    for num in list2:
        check[num] = True
    for num1 in list1:
        if num1 not in check:
            print(num1, "is the missing element")
            return num1


find_missing_using_ht([4, 9, 12, 69, 5], [69, 4, 12, 9])
'''
'''
This is O(n), but at the cost of some extra space, O(n) to be exact.
'''
'''
But what if you don't have extra space, and still want to do it in O(n), you can think of sets
'''
'''
------------------------------------------------------------------------------------------------------------------------
If there's ONLY ONE element, that is missing, WHY NOT JUST GET THE DIFFERENCE OF SUMS OF BOTH LISTS?

def find_missing_using_sums(list1, list2):
    return sum(list1)-sum(list2)

print(find_missing_using_sums([4, 9, 12, 65, 5],[65, 9, 12, 4]))
'''


'''
------------------------------------------------------------------------------------------------------------------------
def missing_element_using_sets(list1, list2):
    #missing = set(list1).difference(set(list2))
    missing = set(list1) - set(list2)
    return list(missing)[0]


print(missing_element_using_sets([4, 9, 12, 69, 5], [69, 12, 4, 9]))
'''

'''
Analysis:
    TC: O(n) + O(n) for converting the lists into sets, that boils down to O(n)
        and an additional O(n) for the difference operation on those sets
        
    SC: No extra space
    
    This is the best we did till now, no extra space and linear time,
    There is no way you can find the missing element in less than O(n) unless the given list is specified as sorted
'''

'''
------------------------------------------------------------------------------------------------------------------------
def missing_element_with_xor(list1, list2):
    xor_sum = 0
    for num in list1:
        xor_sum ^= num
    for num in list2:
        xor_sum ^= num
    return xor_sum


print(missing_element_with_xor([4, 9, 12, 69, 5], [12, 69, 9, 4]))

'''
'''
(x ^ y) = z
(z ^ y) = x
(z ^ x) = y
'''

'''
The above three lines seem to be a property of 3 numbers by doing xor on three of them, 
so based on that, if we consider, 4, 9, 12, 69 (xors) as x and do it with 5, which is y
 x ^ y = z
 
 now, with z we are doing xor with everything other than one number (which is the missinh one in our case)
 so, as z ^ x gives us y, we get 5 as the output
'''

'''
TC: O(n)
SC: O(1)
'''



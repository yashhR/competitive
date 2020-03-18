'''
Given an array of numbers and a target, return the indices of two numbers that sum up to that target
You can assume that:
    1. Each input has exactly one solution
    2. Cannot use the same element twice
'''

'''
-----------------------------------------------------------------------------------------------------------------------
Brute-force approach:

In this, we go loop through all the elements in the array, and for every element, we loop through the rest
of the array checking if they both sum up to the target, if they do - we return, if NOT, we move to next element.


nums = [2, 7, 11, 15]
target = 9


def two_sum_bf(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum_bf(nums, target))   # Output : [0, 1]


Analysis:

This is brute-force, for each element we are looping through the rest of the elements, so that's O(n^2)
TC: O(n^2)
SC: O(1)
'''

'''
------------------------------------------------------------------------------------------------------------------------
How can we do better? Again, if we are gonna have to check if there is a compliment for every element, and that too
for every element, we better have a hash-table that saves us the lookup time.

Create a dictionary that has nums as keys and indices of nums as values
for every element, see if compliment exists in seen dictionary, and if it does, return the value.

nums = [2, 7, 11, 15]
target = 9


def two_sum_hash(nums, target):
    seen = {}
    for idx in range(len(nums)):
        seen[nums[idx]] = idx
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in seen:
            return [i, seen[compliment]]


print(two_sum_hash(nums, target))       # Output: [0,1]

'''

'''
-----------------------------------------------------------------------------------------------------------------------
But we aren't really utilizing the looping that we are doing to create the hash table.

What we can do is,

every time we loop through the hash table itself, we see if the compliment exists in hash table, if it does, 

we return the compliment's index first and then the index of the element we were about the insert into the table
'''

nums = [2, 7, 11, 15]
target = 9
seen = {}


def two_sum_in_one_pass(nums, target):
    for idx, num in enumerate(nums):
        compliment = target - num
        if compliment not in seen:
            seen[num] = idx
        else:
            return [seen[compliment], idx]


print(two_sum_in_one_pass(nums, target))         # Output: [0, 1]


'''
Learnings and take-aways:

1. Use hash tables for lookups
2. When creating hash tables, store the indices as the values in the dictionary instead of any dummy value
3. Use the enumerate option to do the above:
    enumerate works as below:
    for idx, num in enumerate(nums):
    -- the unpacking is done in a way that the idx takes value 0, as default, and num takes the values in the array
       you can change the way you start evaluating the idx values.
       
    for idx, num in enumerate(nums, 100) -- here 100 acts as the starting value of idx,
    
    DO NOT GET CONFUSED BETWEEN THE ORDER OF THE MAPPING.
    the unpacking IS NOT DONE respectively.
4. Utilize the values when you are looping through the array in the process of creating the hash table
 
'''
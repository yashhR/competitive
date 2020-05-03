'''
Number of subarrays having sum exactly equal to k
Given an unsorted array of integers, find the number of subarrays having sum exactly equal to a given number k.

Examples:

Input : arr[] = {10, 2, -2, -20, 10},
        k = -10
Output : 3
Subarrays: arr[0...3], arr[1...4], arr[3..4]
have sum exactly equal to -10.

Input : arr[] = {9, 4, 20, 3, 10, 5},
            k = 33
Output : 2
Subarrays : arr[0...2], arr[2...4] have sum
exactly equal to 33.
'''

'''
The NOT smart version is to get all the subarrays and see with the sum is equal to k, if yes increment count
'''


'''
Brute-force approach (Approach 1)
'''

# nums = [9, 4, 20, 3, 10, 5]
# k = 33
# count = 0
# n = len(nums)
# for i in range(n):
#     for j in range(i, len(nums)):
#         if sum(nums[i:j+1]) == k:
#             print(nums[i:j+1])
#             count += 1
# print(count)

# It is worth noticing for minor optimization that - if the given array has non negative integers only,
# then at any point, if the sum(subarray) is greater than k, then we can abort the second index j and skip to the next
# first index i because, adding on non negative integer values to a value already greater than k will only increase sum
# so, skipping that saves us a little time.



'''
Approach 1 is O(n^2) and pretty slow! and we are going to have to do better than that!

The cumulative sum approach is the best shot in problems like these.
The base idea comes from the logic that when calculating the cumulative sum, if we store the cumulative sum that
we have obtained at different points of the array, and if we have come across a sum twice, then that means that
everything between the previous time we have seen that sum and the present position - all those numbers add up to 0.


[1, 2, 3, -2, 0, 1, 1, 4]
the below array corresponds to cumulative sum at each index of the above array:
[1, 3, 6, 4, 0, 5, 6, 10]

If observed, we can see that we have got the sum of 6 twice in the array, at index 2 and index 6 --
and that all numbers from 3 to 6 add up to 0 (-2+0+1+1)
That means we have a subarray that has the sum as zero (0)
This will be useful to find out the number of subarrays with sum ZERO.


Following the same logic, to see if a subarray of sum k exists, all we have to do is, store all the unique sums that
we have got while calculating the cumulative sum and also store the frequency of the number of times we have seen a 
particular sum. Now, at every new addition, we see if the current cummulative sum minus k (currsum - k) is already seen
in the array and if we have, then we increment the number of subarrays by the frequency of the currsum - k


This works because, now we are at a particular current sum and if we have seen currsum-k previously, then that means
the subarray between current posn and the posn where currsum-k is present has the sum equal to k. 
'''
nums = [10, 2, -2, -20, 10]
seen_sums = {0: 1}
cum_sum = 0
subarrays = 0
k = -10
for num in nums:
    cum_sum += num
    if cum_sum - k in seen_sums:
        subarrays += seen_sums[cum_sum-k]
    if cum_sum not in seen_sums:
        seen_sums[cum_sum] = 1
    else:
        seen_sums[cum_sum] += 1
print(subarrays)

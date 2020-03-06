'''
The famous coin change problem:
    -- Asked in most product based companies, mostly in Amazon
    -- One of the premium questions on LeetCode
    -- A great demonstration of the programming paradigm of dynamic programming

The coin change problem is as follows (in my words):

You are given a set of different coins {S1, S2, S3, ....}, and also a specific change (N)

The task is to find out in HOW MANY UNIQUE WAYS YOU CAN GET THE CHANGE USING THOSE SET OF COINS

Ex: Let's say you have the coins: Rs.1, Rs.2, and Rs.5.
    You have to make the change for Rs.5
    Note: You have an infinite number of the coins of given denominations

    Solution:
                {5} = 5
                {1, 1, 1, 1, 1} = 5
                {1, 2, 2} = 5
                {1, 2, 1} = 5


    Imagine you have 3 bags, one bag each containing coins of Rs.1, Rs.2 and Rs.5 and your bill is Rs.5

    If you look at the solution and think about it, we have the choice of using a specific coin
    or not using the same coin when making the change:






'''
'''
Given an amount and the denominations available, we are asked to calculate the minimum number of coins
that make up that amount

Don't think greedy, here's why:

For an amount of 31 and denominations of 25, 10, 1
Greedily, we might be tempted to think that we will directly put the largest denomination coin first so that
we take out most of the values.

But in that case, the number of coins will be 1*25 + 6*1 making it 7 coins
But the best case is, 3*10 + 1*1 making it 4 coins

!DO NOT THINK GREEDY!
'''

denominations = [25, 10, 1]
lookup = [0]


def min_coins(cents):
    for i in range(1, cents+1):
        lookup.append(100)
    for i in range(1, len(lookup)):
        for j in range(len(denominations)):
            if i >= denominations[j]:
                lookup[i] = min(lookup[i], lookup[i-denominations[j]]+1)
    return lookup[-1]


print(min_coins(31))


'''
The above is a classic dynamic programming approach to the solution.
The solution demonstrated above is the bottonm-up approach.

So, how this works is that:
    we try to make change for all the possible values within the range of the amount
    i.e., if the amount we wanna make the change for is 31
    we calculate the minimum change for all the values within 31.
    i.e., we make minimum change for 0, 1, 2, 3, 4 ... 31
    
    And the way we find out the minimum number of coins, is by trying each coin in the denomination, 
    and because that results in a lesser amount, i.e., for 31, if we used 25, then we will look for the
    minimum coins that can make up 31-25 which is 6, for which we would have already calculated the
    minimum coins. THIS IS WHY WE GO BOTTOM UP.
    
    Here, it is important to notice that, we choose all the coins, that is, we use 25 once, 10 once, and 1 once,
    and because for each usage of coin, we get a lesser amount, we refer to the minimum number of coins that will
    be used to make up that amount: 31-25 = 6, 31-10 = 11, 31 - 1 = 30. We go to 6, 11, 30 and see which one of
    them has the minimum number of coins used and then we add one to it because we just used each one of these,
    we get the minimum of 3 and we return it. Because we are going to build through it, we need to store the 
    already calculate min coins of all amounts in an array. (Memoization part of our DP approach!)
    
    Because we are going bottom-up, lets start finding out the minimum number of coins that would be used to make the
    change of 0, 1, 2 ... and build up to the asked amount.
    
    Let's keep account of all of these in a list called lookup.
    This needs to be store the min of all amounts starting from 0 to the asked amount, which means,
    the length of the list needs to be amount + 1.
    For 0, the min number of coins is 0
    For 1, we see the denominations:
           we got 25 -- can we use it? NO
           we got 10 -- can we use it? NO
           we got 1 --  can we use it? YES 
                    So, use it. If you use it, you have used 1 coin.
                    Now, what is the remaining amount? 0. Go to 0 and check the min coins for 0. it is 0.
                    So, add 0 + 1, that is the minimum number of coins for making the change of 1 using given denoms
                    lookup[1] = 1
    For 2, we see the denoms:
           we got 25 -- can we use it? NO
           we got 10 -- can we use it? NO
           we got 1 --  can we use it? YES 
                    So, use it. If you use it, you have used 1 coin.
                    Now, what is the remaining amount? 1. Go to 1 and check the min coins for 1. it is 1.
                    So, add 1 + 1, that is the minimum number of coins for making the change of 2 using given denoms
                    lookup[2] = 2
    For 3, we see the denoms:
           we got 25 -- can we use it? NO
           we got 10 -- can we use it? NO
           we got 1 --  can we use it? YES 
                    So, use it. If you use it, you have used 1 coin.
                    Now, what is the remaining amount? 2. Go to 2 and check the min coins for 2. it is 2.
                    So, add 2 + 1, that is the minimum number of coins for making the change of 1 using given denoms
                    lookup[3] = 3
    .
    .
    .
    .
    .
    
    This trend goes on until 9, because obviously the only way you can make these by using 1 those many number of times.
    
    For 10, we see the demons:
           we got 25 -- can we use it? NO
           we got 10 -- can we use it? YES
                     So, use it. If you use it, you have used 1 coin.
                     Now, what is the rem amount? 0. Go to 0, and check the min coins for 0. It is 0.
                     So, add 0 + 1, that is the min num of coins to make change of 10 using given denoms
                     lookup[10] = 1.
        We are not done yet.
           we got 1 -- can we use it? YES
                     So, use it. That's 1 coin.
                     Now, what is the rem amount? 9. Go to 9 and check, that's 9.
                     Add 9 + 1, that's 10. Compare 10 to what is already in the lookup = 1
                     minimum of 1, 10? 1
                     lookup[10] = 1
                     
    For 11, we see the demons:
           we got 25 -- can we use it? NO
           we got 10 -- can we use it? YES
                     So, use it. If you use it, you have used 1 coin.
                     Now, what is the rem amount? 1. Go to 1, and check the min coins for 1. It is 1.
                     So, add 1 + 1, that is the min num of coins to make change of 11 using given denoms
                     lookup[11] = 2.
        We are not done yet.
           we got 1 -- can we use it? YES
                     So, use it. That's 1 coin.
                     Now, what is the rem amount? 10. Go to 10 and check, that's 1.
                     Add 1 + 1, that's 2. Compare 2 to what is already in the lookup = 2
                     minimum of 2, 2? 2
                     lookup[11] = 2
    .
    .
    .
    .
    .
    .
    
    This trend goes on until 19
    lookup[19] becomes one 10 coin and nine 1 coins
    lookup[19] = 1 + 9 = 10
    .
    .
    .
    .
    .
    
    For 20, we got 25? CANT USE IT
            we got 10? YO USE IT NIGGER
                    If you have used it, that's 1 coin.
                    Whats the rem amount? 10. Go to 10 and check the min coins for making 10, that's 1
                    So, lookup[20] becomes 1+1 i.e., 2
                    lookup[20] = 2
            we got 1? USE IT
                    If you use it, that's 1 coin.
                    Whats the rem amount? 19. Go to 19, check, whats the min? 10
                    that's 11 coins, is it better than 2, which is already in place? NO
                    So, 
                    lookup[20] = 2
    
    
    For 21, we got 25? CANT USE IT
            we got 10? YO USE IT NIGGER
                    If you have used it, that's 1 coin.
                    Whats the rem amount? 11. Go to 11 and check the min coins for making 11, that's 2
                    So, lookup[21] becomes 1+2 i.e., 3
                    lookup[21] = 3
            we got 1? USE IT
                    If you use it, that's 1 coin.
                    Whats the rem amount? 20. Go to 20, check, whats the min? 2
                    that's 3 coins, is it better than 3, which is already in place? ITS THE SAME
                    So, 
                    lookup[21] = 3
    .
    .
    .
    .
    .
    .
    .
    
    For 25, we got 25, can we use it? YES
                        If you use it, that's 1 coin.
                        Go to 25-25 (rem) and check min for that, that's 0
                        so,
                        lookup[25] = 1
    .
    .
    .
    .
    .
    .
    .
    
    For 31, we got 25, can we use it? YES
                If you use it, that's 1 coin.
                Go to 31-25, the rem is 6, go to 6 and see the min of 6 => 6
                So, add 1+6, 7
                lookup[31] = 7
            we got 10, can we use it? YES
                If you use it, that's 1 coin.
                Go to 31-10, the rem is 21, go to 21 and check the min coins => 3
                So, add 1 + 3, 4
                lookup[31] = 4
            we got 1, can we use it? YES
                If you use it, that's 1 coin.
                Go to 31-1, the rem in 30, go to 30 and check min coins => 3
                So, add 1 + 3, 4
                lookup[31] = 4
                
Minimum of 7, 4 and 4 is 4.
So that will take the place.
             
'''

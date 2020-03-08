'''
Writing programming interview questions hasn't made me rich yet ...
so I might give up and start trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and
returns the best profit I could have made from one purchase and  one sale of one share of Apple stock yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

No "shorting"—you need to buy before you can sell.
Also, you can't buy and sell in the same time step—at least 1 minute has to pass.
'''

stock_prices = [10, 7, 5, 8, 11, 9]


def get_max_profit(s):
    pEach = []
    n = len(s)
    for i in range(n-1):
        temp = []
        for j in range(i+1, n):
            if len(temp) > 0:
                if s[j] - s[i] > temp[-1]:
                    temp.append(s[j]-s[i])
            else:
                temp.append(s[j]-s[i])
        if len(pEach) > 0:
            if temp[-1] > pEach[-1]:
                pEach.append(temp[-1])
        else:
            pEach.append(temp[-1])
    return pEach[-1]


print(get_max_profit(stock_prices))

'''
This was a practice question on interviewcake.com under the category: AMAZON INTERVIEW QUESTIONS

This solution tested OK for all inputs

test_error_with_empty_prices (__main__.Test) ... ok
test_error_with_one_price (__main__.Test) ... ok
test_price_goes_down_all_day (__main__.Test) ... ok
test_price_goes_down_then_up (__main__.Test) ... ok
test_price_goes_up_all_day (__main__.Test) ... ok
test_price_goes_up_then_down (__main__.Test) ... ok
test_price_stays_the_same_all_day (__main__.Test) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
'''
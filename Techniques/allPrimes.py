'''
Given a number N, find all the prime numbers with the range as 1 to N (1:N]
Ex: N = 21
    allPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 21]



                        --------------------   Naive approach  --------------------------

        This is the brute-force approach.
        As we know, a prime number is a number which is divisible by 1 and itself (2 divisors)
        So, we first write a function that checks whether a number is prime or not

        def isPrime(n):
            count = 0                # a counter to keep track of how many divisors the number has
            for i in range(1, n+1):  # range starts from 1 to avoid division by zero error, n+1 because n inclusive
                if n % i == 0:
                    count += 1       # if divisible, increment counter by 1
            if count == 2:           # if the number of divisors is 2, we return True
                return True
            return False

        Now that we have a function, all we have to do is to go through every number in the range and check if Prime/not

        def noOfPrimes(N):
            allPrimes = []               # A list to store all the prime numbers
            for i in range(2, N+1):      # Excluding 1 because it has only one divisor (itself)
                if isPrime(i):
                    allPrimes.append(i)
            return allPrimes

        Note: When going through the range for counting divisors, the better option is
        to only traverse through 2, sqrt(N) because number above sqrt(N) cannot divide N anyway,
        so no point of comparing

                        --------------------   Sieve approach  --------------------------

        The problem with the above approach is:
        -- we know all multiples of 2 (evens) are not prime, so we don't have to check for them
        -- we know all multiples of any number we traverse through are not prime, we don't have to check for them
        In this way, when we go through the range, if we remove the multiples of a number, our checks will
        drop down drastically leading to better time complexity

        Sieve approach is basically eliminating the multiples of all numbers in the range, and whatever remains
        are obviously the prime numbers

        1. We get all the numbers in the range:
            all = []                        # list in which we store all the numbers
            for i in range(2, n+1):         # excluding 1 because removing multiples of 1 means removing all elements XD
                all.append(i)
            for i in range(2, n+1):
                x = i*2                     # we want to remove the multiples of the number, not the number itself
                while x <= n:               # Can't remove numbers above n, because they are not in all list
                    try:
                        all.remove(x)       # try and except because for example, when i = 2, we remove 4,6,8,10,12..
                    except ValueError:      # and when i=3, we are asking to remove 6,9,12 which were already removed
                        pass                # so to escape the error, we try to remove, if not there, we just pass
                    x = x + i
            print(all)

'''


n = 33456
all = []
for i in range(2, n+1):
    all.append(i)

for i in range(2, n+1):
    x = i*2
    while x <= n:
        try:
            all.remove(x)
        except ValueError:
            pass
        x += i
print(all)                  # Output [2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ... 33391, 33403, 33409, 33413, 33427]


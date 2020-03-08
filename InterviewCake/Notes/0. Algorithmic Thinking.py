'''
[Big-O notation:
This is the language we use to express our runtime in terms of how it changes with:
                                                            -- size of the input
                                                            -- as input size becomes arbitrarily large
Basically, we are scaling data and asking ourselves how the runtime changes if the input size changes
Often times, we have different ways to solve the same problem and we would want to know which approach (algorithm)
is the best for our use case.]


With Big-O analysis, we express our runtime in terms of - 1.how quickly it grows
                                                          2.relative to the size of the input
                                                          3.as input gets arbitrarily large
Best to break it down into these three sentences:

1. how quickly it grows:
    We aren't tying to know the exact runtime. It depends on a lot of things like the processor of the
    PC you're running it on, what other applications the computer is running, etc.,
    WE WANT TO ANALYZE THE ALGORITHM ALONE, so thinking of it in terms of exact runtime is not correct
    because it changes from device to device.


2. relative to the size of input:
    We can't measure it in terms of the exact runtime, but we want to express how it grows, so we need to
    express the growth in terms of something that's not platform dependant (whether you are using Python, C++)
    or on the device you are running it on. Some criteria that depends on the algorithm alone.
    That is the input size. No matter what language or device we are using, we are going to use the same logic,
    same input. So, thinking of runtime in terms of size of the input makes sense.


3. as input gets arbitrarily large:
    This is important because we don't want to check the algorithm for smaller values and decide how good it is.
    but when actually using it in practical scenarios, we might be surprised how it becomes opposite of what we
    observed with inputs of smaller sizes.

    BEST EXAMPLE:
    The time complexities of Bubble Sort and Quick Sort. [O(N^2) and O(N*logN) respectively]

    Suppose we want to sort an array of integers,
    we have two algorithms as stated above, Bubble and Quick Sort
    For an array of smaller sizes, like 10:
    we observe that Bubble sort takes lesser time than Quick sort,
    but that is not the case for larger sizes, say a 1000, we observe quick is better than sort

    Quick sort may do expensive steps for smaller sizes but with increase in size, the same expensive
    steps make the algorithm work better than bubble.

    This is an example of why looking at the exact runtime is NOT a sensible thing to do even if the same machine,
    we consider how it grows to all sizes of input, not just smaller sizes


    Expression:
    (Order of) (Big-O of) all need to be expressed as O()

    N is the input/input size, and we write the expression in the parenthesis of O(<here>) in terms of N
    The expression can be linear, quadratic, cubic, constant etc.,

RULES:
    1. N can be the just the input or the size of the input.

    Ex: 1. N can just be an integer:
        def say_hi(n):
            for each in n:
                print("Hi")

        2. N can be size of the input:
            arr = ["Raahel", "Roshan", "Ruhi"]
            def say_hi_to(arr):
                for name in arr:
                    print("Hi,", name)



    2. Drop the constants.
        In the expression that we write in the Big-O parenthesis, we only consider the most significant term
        and ignore the constants

    Ex: Print the first element, print half of elements, say hello 100 times
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        def first_half_hundred(arr):
            print(arr[0])

            middle = len(arr)//2
            i = 0
            while i<=middle:
                print(arr[i])

            for i in range(100):
                print("Hi")

        Break it down, what part of the function is actually depending on the input?

        1st element accessing won't change no matter the size of input
        Printing hello 100 times is same for 2 elements or 1000 elements, so not dependent on input

        Only the printing half elements part changes with input,
        if size is 10, we print 5 times
        if size is 1000, we print 500 times (obviously, dependant)

        So, O(1 + n/2 + 100) becomes O(n)
        DROP THE CONSTANTS


    3. DROP THE LESS SIGNIFICANT TERMS:

        If expression is quadratic, like O(5n^2 + 100n + 25) => O(n^2)



    4. Always express the worst case:

        needle, haystack example
        In a haystack, check if needle is present in it or not, if it does, where?

        for item in haystack:
            if item == needle:
                return True
        return False

        Here, the needle can be present in the 1st place, which is best scenario O(1) - constant time
            the needle isn't even there, which means you check all items -- O(n) - linear time

        so, the time complexity of the algorithm is O(n)
'''


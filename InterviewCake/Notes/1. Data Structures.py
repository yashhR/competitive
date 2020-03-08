'''
Random Access Memory:

RAM is volatile, temporary memory that is useful when running a program or an application
In the program files, we will have to store the variable at a place so that we can access it later on in the program

RAM is where all of these are stored. But this is temporary, we DO NOT want to permanently store these variable
values.

Think of RAM as a bookcase with billions of shelves, like actually picture it -- a billion shelves
Each shelf has an address [0, 1, 2, 3, 4 .... billion]

Now, each shelf can store 8 bits, a bit is like an electric switch you can ON or OFF i.e., 1 or 0
8 bits is a byte. So, we can say each shelf has a byte of memory

But why do we call it as RANDOM ACCESS MEMORY:

    So, there's a processor that does the reading and writing of data from the memory
    Now, In between the processor and the RAM, there's something called a MEMORY CONTROLLER which has
     A DIRECT CONNECTION TO EVERY ADDRESS IN THE RAM

     The point of memory controller having a direct connection (with all the shelves) all the addresses is
     the key to understanding RAM. This means the memory controller can access the contents of address 0, address 69,
     address 420, address, 6969 etc., in the same FRICKING time.

     So, you can choose an address RANDOMLY in the MEMORY, and we have A DIRECT ACCESS to it through the memory controller
     Hence, calling it RANDOM ACCESS MEMORY

    BUT there's a catch here,
    if we can measure the time taken between accessing an address X and address Y, we might think it is a constant
    difference irrespective of the addresses. BUT computers can access addresses faster if X and Y are closer.

    This is because of something called CACHE MEMORY.
    When the processor asks for contents at an address X, the memory controller gives its contents in constant time,
    in addition to that, IT ALSO SENDS in the contents of nearby addresses, the processor didn't ask for it, but still
    the mem contr sends it because it is likely that the next address could be close to X

    So, if processor asks for contents at address 953, mc sends byte at 953, and along with it, it sends bytes
    at 954, 955, 956 et., these are stored in the processor as CACHE MEMORY

    so, next time if processor needs 955, it first checks in cache memory, and because its present, it uses it.
    CACHE MEMORY IS LIKE, SUPER FAST. But its not helpful if the next address is not close to the current one.
'''

print("\nQuestion 2:")
integer = 1
numLoops = 0
flag = True
print("(0) ", end="")
while flag:
    numLoops = numLoops + 1
    print(("{0} \n({1}) {0} / 2 = ".format(integer, numLoops)), end="")
    smallestNumber = integer
    integer = integer / 2
    if integer == 0:
        flag = False
        print('  0')

print("Epsilon is --> {}".format(smallestNumber))
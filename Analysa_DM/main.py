# Author : Nitzan Tomer & Zaccharie Attias.
# Assignment Number One


# Question Two Variables
ourEpsilon = 0
arbitraryNum = 1
loopsNum = 0
flag = True

# Question Two Function Solution
print("[Question Two]")
while flag:
    print(f'({loopsNum}) {arbitraryNum} \ 2 = {arbitraryNum / 2}')
    loopsNum = loopsNum + 1
    ourEpsilon = arbitraryNum
    arbitraryNum = arbitraryNum / 2
    if arbitraryNum == 0:
        flag = False
print(f'Your Epsilon Is --> {ourEpsilon}\n')


# Question Three Solution
print("[Question Three]")
print("The Original Calculation --> " + str(abs(3.0 * (4.0 / 3.0 - 1) - 1)) + "\n")


# Question Four Solution
print("[Question Four]")
print("The Fixed Equation --> abs(round(3.0*(4.0/3.0-1)-1))")
print("The Fixed Solution --> " + str(abs(round(3.0 * (4.0 / 3.0 - 1) - 1))))

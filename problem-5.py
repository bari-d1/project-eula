# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
i = 2520
j=19
upperLimit = 19
increment = 20

def check_lcm(big, small):
    inc = big
    while True:
        if (inc % small == 0):
            return inc
        else:
            inc += big
    

while True:
    if i%j == 0 and j > 10:
        j-=1
        increment = check_lcm(increment, upperLimit)
        upperLimit -= 1
        print(i,j)
    else: 
        i+=increment
        j=upperLimit
        print(i,j)
    if j == 10:
        break

print(i)

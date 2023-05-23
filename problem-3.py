# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import time
import math

num = 600851475143
multiple = 0

def check_prime (number):
    prime = True
    for i in range(2,((number//2)+1)):
        if i != 1 and number%i == 0:
            prime = False
            break
    return prime

start = time.time()
if check_prime(num) == False:
    for i in range(1,math.floor((math.sqrt(num)))):
        if check_prime(i) == False and check_prime(num//i) == False :
            print(i)
            continue
        elif num%i == 0 and check_prime(i) == True:
            multiple = i
            print(multiple)
        elif num%i == 0 and check_prime(num//i) == True:
            multiple = num//i
        print(str(i) + ","+ str(multiple))
# print(multiple)
end = time.time()

print(end-start)
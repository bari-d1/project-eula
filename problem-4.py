# A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
palindrome = 0
def check_palindrome(num):
    txt = str(num)
    if txt[::-1] == txt:
        return True
    else: return False

for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        if check_palindrome(product) and product > palindrome:
                palindrome = product
                print(i,j,palindrome)

print(palindrome)

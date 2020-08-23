from utils.check_palindrome import CheckPalindrome

result = []
for i in range(1,1000000):
    if CheckPalindrome(i) and CheckPalindrome(int(bin(i).replace("0b",""))):
        result.append(i)

print(sum(result))

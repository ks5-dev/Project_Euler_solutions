from utils.check_palindrome import CheckPalindrome
def find_largest(n):
    result = 0
    for i in range(100,n):
        for j in range(100,n):
            pro = i*j
            if CheckPalindrome(pro):
                result = max(result,pro)
    return result

print(find_largest(1000))

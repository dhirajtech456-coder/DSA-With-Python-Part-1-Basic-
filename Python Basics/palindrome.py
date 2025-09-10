def checkPalindrome(s):
    if s==s[::-1]:
        print("Its palindrome ")
    else:
        print("its' not a palindrome")
print(checkPalindrome("Mausam"))
print(checkPalindrome("madam"))
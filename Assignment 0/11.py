n = input("Enter a string: ")

def reverse(s):
    return s[::-1]
def palindrome(s):
    rev = reverse(s)
    if s.lower()==rev.lower():
        return True
    else:
        return False

a = palindrome(n)
if a:
    print("Yes, {} is a palindrome".format(n))
else:
    print("No, {} is not a palindrome".format(n))

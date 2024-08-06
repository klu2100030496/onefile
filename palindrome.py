def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Test the function
test_string = "A man, a plan, a canal, Panama"
print(f"'{test_string}' is a palindrome: {is_palindrome(test_string)}")
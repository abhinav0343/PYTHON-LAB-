def min_operations_to_palindrome(s):
    n = len(s)
    operations = 0
    for i in range(n // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        if left_char != right_char:
            operations += abs(ord(left_char) - ord(right_char))
    return operations
#ord function read the unicode point(integer represenation)
#abs function returns absolute value of integer ensures the integer is non-negative
T = int(input("enter number of test cases : "))
for _ in range(T):
    s = input("string : ").strip() # strip function removes white spaces including \t,\n.
    print(f"minimum operations is : {min_operations_to_palindrome(s)}")

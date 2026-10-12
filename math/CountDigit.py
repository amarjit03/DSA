"""
Given a number n, return the count of digits in this number.

Example:

Input: n = 1567
Output: 4
Explanation: There are 4 digits in 1567, which are 1, 5, 6 and 7.

Input: n = 255
Output: 3
Explanation: There are 3 digits in 255, which are 2, 5 and 5

"""

# Iterative Solution O(log10(n)) Time or O(Number of digits) and O(1) Space

# def countDigit(n):
#     if n == 0:
#         return 1
#     count = 0
#     while n != 0:
#         n = n//10
        
#         count += 1
    
#     return count

# if __name__ == "__main__":
#     n = 58964
#     print(countDigit(n))


# Using Recursion - O(log10(n)) or O(Number of digits) Time and O(Number of digits) Space

# def countDigit(n):
    
#     if n // 10 == 0:
#         return 1
#     return 1+ (countDigit(n//10))

# if __name__ == "__main__":
#     n = 58964
#     print(countDigit(n))

# Converting Number to String - O(Number of digits) Time and O(Number of digits) Space    
    
def countDigit(n):
    # Convert integer to string
    num = str(n)

    # If negative, exclude '-' sign
    if num[0] == '-':
        return len(num) - 1

    return len(num)

if __name__ == '__main__':
    n = -58964
    print(countDigit(n))
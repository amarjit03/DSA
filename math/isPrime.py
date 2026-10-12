"""
Given a number n, check whether it is a prime number or not.
Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Input: n = 7
Output: true
Explanation: 7 is a prime number because it is greater than 1 and has no divisors other than 1 and itself.

Input: n = 25
Output: false
Explanation: 25 is not a prime number because it is divisible by 5 (25 = 5 × 5), so it has divisors other than 1 and itself.

Input: n = 1
Output: false
Explanation: 1 has only one divisor (1 itself), which is not sufficient for it to be considered prime.

"""

def isPrime(n):
    
    if n <= 1:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
  n = 12
  if(isPrime(n)): 
    print("true")
  else:
    print("false")
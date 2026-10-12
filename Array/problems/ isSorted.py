"""
Given an array arr[], check if it is sorted in ascending order or not. 
Equal values are allowed in an array and two consecutive equal values are considered sorted.


Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.

Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.


"""

# Iterative approach - O(n) Time and O(1) Space


def isSorted(arr) -> bool:
    
    n = len(arr)
    
    for i in range(1,n):
        if (arr[i-1] > arr[i]):
            return False
    return True

if __name__ == "__main__":
    arr = [10,20,30,40]
    if (isSorted(arr)):
     print("true")
    else:
     print("false")
        



"""
Given an array arr[], replace each element with the product of itself and its adjacent elements.

For index i:

arr[i] = arr[i-1] * arr[i] * arr[i+1]
Assume the previous of the first and the next of the last as 1.

Examples:

Input: arr[] = [2, 4, 5]
Output: [8, 40, 20]
Explanation: 
For index i = 0, arr[0] = 1 * arr[0] * arr[1] = 1 * 2 * 4 = 8
 For index i = 1, arr[1] = arr[0] * arr[1] * arr[2] = 2 * 4 * 5 = 40
 For index i = 2, arr[2] = arr[1] * arr[2] * 1 = 4 * 5 * 1 = 20
Thus, the updated array becomes [8, 40, 20].

Input: arr[] = [2, 5, 7, 8, 3]
Output: [10, 70, 280, 168, 24]
Explanation: 
For index i = 0, arr[0] = 1 * arr[0] * arr[1] = 1 * 2 * 5 = 10
 For index i = 1, arr[1] = arr[0] * arr[1] * arr[2] = 2 * 5 * 7 = 70
 For index i = 2, arr[2] = arr[1] * arr[2] * arr[3] = 5 * 7 * 8 = 280
 For index i = 3, arr[3] = arr[2] * arr[3] * arr[4] = 7 * 8 * 3 = 168
 For index i = 4, arr[4] = arr[3] * arr[4] * 1 = 8 * 3 * 1 = 24
Thus, the updated array becomes [10, 70, 280, 168, 24].


"""


# def updateArray(arr):
#     n = len(arr)
    
#     temp = [0] * n
    
#     for i in range(n):
        
#         prev = 1 if i == 0 else arr[i - 1]
            
#         next_ele = 1 if i == n - 1 else arr[i + 1]
            
#         temp[i] = prev * arr[i] * next_ele
    
#     print(temp)

# arr = [2, 4, 5]

# updateArray(arr)



def updateArray(arr):
    n = len(arr)
    
    temp = [0] * n
    
    prev = 1
    
    for i in range(n):
        
        curr = arr[i]
        
        next_ele = 1 if i == n - 1 else arr[i + 1]
        
        temp[i] = prev * curr * next_ele
    
    print(temp)

arr = [2,4,5]
updateArray(arr)
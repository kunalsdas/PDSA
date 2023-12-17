'''
Find the first occurrence in the sorted list, Write a function findFirstOccurrence(L, k) that accepts a sorted list L of integers and an integer k.
The function returns the index of the first occurrence of element k in the list L from the left. If k is not present in list L, then return -1.
Write an efficient solution of the complexity O(log n)
Note:- Do not use slicing in solution code for the list because it is O(n) operation.
Sample Input
[1,1,1,2,2, 3,3,3,3,3,4,4]
3
Output
7
'''

def findFirstOccurrence(L, k):
    left = 0
    right = len(L) - 1
    result = -1 

    while True:
        mid = (left + right) // 2
        if L[mid] == k:
            result = mid
            right = mid - 1 
        elif L[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return result
L=[1,1,1,2,2,3,3,3,3,3,4,4]
k=2
print(findFirstOccurrence(L,k))

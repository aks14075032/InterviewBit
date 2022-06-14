#Problem -- https://www.interviewbit.com/problems/max-min-05542f2f-69aa-4253-9cc7-84eb7bf739c4/

def getMinMax(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]
    
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)
    
    elif high == low+1:
        if arr[high] > arr[low]:
            arr_max = arr[high]
            arr_min = arr[low]
        else:
            arr_max = arr[low]
            arr_min = arr[high]
        return (arr_max, arr_min)
    else:
        mid = int((low+high)/2)
        arr_max1, arr_min1 = getMinMax(low, mid,arr)
        arr_max2, arr_min2 = getMinMax(mid+1, high, arr)
    
        return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxi, mini = getMinMax(0, len(A)-1, A)
        return maxi+mini
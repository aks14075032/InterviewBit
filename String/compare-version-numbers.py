class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        arr1 = A.split(".")
        arr2 = B.split(".")

        n = len(arr1)
        m = len(arr2)

        arr1 = [int(i) for i in arr1]
        arr2 = [int(i) for i in arr2]
        # print('Hello1 --> ',arr1)
        # print('Hello2 --> ', arr2)
        if n > m:
            for i in range(m, n):
                arr2.append(0)
        elif m > n:
            for i in range(n, m):
                arr1.append(0)

        for i in range(len(arr1)):
            if arr1[i] > arr2[i]:
                return 1
            elif arr2[i] > arr1[i]:
                return -1
        return 0

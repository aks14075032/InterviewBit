def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


class Solution:
    # @param A : list of integers
    # @return an integer
    def wave(self, A):
        n = len(A)
        A.sort()
        i = 0
        while i < n:
            if i + 1 >= n:
                break
            swapPositions(A, i, i + 1)
            i = i + 2
        return A

# Problem -- https://www.interviewbit.com/problems/pick-from-both-sides/


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        front_list_sum = [0] * len(A)
        back_list_sum = [0] * len(A)
        # print(A)
        for i in range(0, len(A)):
            if i == 0:
                front_list_sum[i] = A[i]
                back_list_sum[len(A) - 1 - i] = A[len(A) - 1 - i]
            else:
                front_list_sum[i] = A[i] + front_list_sum[i - 1]
                back_list_sum[len(A) - 1 - i] = (
                    A[len(A) - 1 - i] + back_list_sum[len(A) - i]
                )

        # print(front_list_sum, back_list_sum)
        answer = max(front_list_sum[B - 1], back_list_sum[len(A) - B])
        for i in range(0, B - 1):
            answer = max(answer, front_list_sum[i] + back_list_sum[i - B + 1])

        return answer

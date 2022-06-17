# Problem -- https://www.interviewbit.com/problems/hotel-bookings-possible/


class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort()
        depart.sort()

        for i in range(len(arrive)):
            if i + K < len(arrive) and arrive[i + K] <= depart[i]:
                return 0
        return 1

#Problem -- https://www.interviewbit.com/problems/merge-intervals/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        n = len(intervals)
        curr = new_interval
        pos = -1
        ans = []
        for i in range(n):
            if max(new_interval.start, intervals[i].start) <= min(new_interval.end, intervals[i].end):
                curr.start = min(curr.start, intervals[i].start)
                curr.end = max(curr.end, intervals[i].end)
            else:
                if curr.end < intervals[i].start:
                    ans.append(curr);
                    pos=i
                    break
                else:
                    ans.append(intervals[i])
        if pos == -1:
            ans.append(curr)
        else:
            for i in range(pos, n):
                ans.append(intervals[i])
        return ans
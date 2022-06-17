# Problem -- https://www.interviewbit.com/problems/merge-overlapping-intervals/hints/

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        ans = []
        n = len(intervals)
        i = 1
        flag = True
        intervals.sort(key=lambda interval: interval.start)
        first = intervals[0].start
        last = intervals[0].end
        while i < n:
            if max(intervals[i].start, first) <= min(intervals[i].end, last):
                if i == n - 1:
                    flag = True
                last = max(last, intervals[i].end)
                first = min(first, intervals[i].start)

            else:
                flag = False
                ans.append(Interval(first, last))
                first = intervals[i].start
                last = intervals[i].end
                if i == n - 1:
                    if max(ans[-1].start, first) <= min(ans[-1].end, last):
                        break
                    else:
                        ans.append(Interval(first, last))
            i += 1

        if flag:
            ans.append(Interval(first, last))

        return ans

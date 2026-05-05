class Solution(object):
    def employeeFreeTime(self, schedule):
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)

        intervals.sort(key=lambda x: x.start)

        res = []
        prev_end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start > prev_end:
                res.append(Interval(prev_end, interval.start))
            prev_end = max(prev_end, interval.end)

        return res
        
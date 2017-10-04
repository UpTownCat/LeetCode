#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_056.py
# @Author: UpTownCat
# @Date  : 2017/10/4

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        results = self.handle(intervals)
        results2 = self.handle(results)
        while len(results) != len(results2):
            results = results2
            results2 = self.handle(results)
        results = sorted(results, key = lambda x: x.start)
        return results
    def handle(self, intervals):
        for i in range(0, len(intervals)):
            interval = intervals[i]
            if not interval:
                continue
            j = 0
            for j in range(0, len(intervals)):
                if i == j:
                    continue
                interval2 = intervals[j]
                if interval2 and interval2.end < interval.end and interval2.end >= interval.start and interval2.start < interval.start:
                    interval.start = interval2.start
                    interval2, intervals[j] = None, None
                if interval2 and interval.start >= interval2.start and interval.end <= interval2.end:
                    interval.start, interval.end = interval2.start, interval2.end
                    interval2, intervals[j] = None, None
                if interval2 and interval.start < interval2.start and interval.end > interval2.end:
                    interval2, intervals[j] = None, None
                if interval2 and interval.start < interval2.start and interval2.start <= interval.end:
                    interval.end = interval2.end
                    interval2, intervals[j] = None, None
        results = list(filter(lambda interval: interval, intervals))
        return results
# intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
# intervals = [Interval(1, 4), Interval(2, 3)]
lists = [[115,121],[319,325],[30,37],[95,101],[445,452],[125,126],[172,172],[29,32],[443,452],[465,466],[420,424],[79,84],[203,206],[352,352],[472,479],[214,221],[124,127],[326,330],[253,254],[351,359],[359,367],[281,284],[188,190],[86,89],[321,322],[106,110],[237,243],[359,359],[431,432],[353,357],[99,106],[343,348],[452,461],[229,234],[91,93],[255,257],[112,120],[185,188],[51,55],[136,140],[27,30],[318,323],[281,281],[57,59],[241,243],[116,118],[181,183],[119,123],[481,482],[191,195],[485,494],[78,86],[39,45],[103,103],[240,249],[167,174],[334,341],[384,389],[367,371],[328,329],[56,62],[5,13],[460,465],[224,228],[178,185],[70,73],[418,427],[113,121],[117,123],[400,407],[308,317],[476,478],[257,260],[110,116],[7,7],[437,442],[438,443],[5,14],[420,421],[193,201],[201,204],[113,122],[412,419],[429,438],[443,443],[238,239],[249,256],[246,254],[280,288],[335,344],[498,502],[54,60],[419,421],[335,344],[493,501],[289,293],[292,295],[166,172],[482,487],[438,443],[277,285]]
intervals = []
for interval in lists:
    intervals.append(Interval(interval[0], interval[1]))
solution = Solution()
# 193,201],[201,204]
intervals3 = [Interval(201, 206), Interval(191, 195), Interval(193, 201), Interval(201, 204), Interval(203, 206)]
for interval in solution.merge(intervals):
    print(interval.start, interval.end)



# results = list(sorted(intervals, key = lambda interval: interval.start))
# for result in results:
#     print(result.start, result.end)
# map(lambda interval: print('[%d, %d]' % (interval.start, interval.end)), solution.merge(intervals))
# for interval ins%d]' % (interval.start, interval.end))
# interval = intervals[2]
# intervals[2] = None
# print(interval.start)

    # if interval.end >= interval2.start and interval.end < interval2.end and interval.start < interval2.end:
    #     interval.end = interval2.end
    #     interval2 = None
    #     intervals[j] = None
    # if interval2 and interval.start <= interval2.start and interval.end >= interval2.end:
    #     interval2 = None
    #     intervals[j] = None
    # if interval2 and interval.start >= interval2.start and interval.end <= interval2.end:
    #     interval.start = interval2.start
    #     interval.end = interval2.end
    #     interval2 = None
    #     intervals[j] = None
    # if interval2 and interval.start == interval2.end:
    #     interval.start = interval2.start
    #     interval2 = None
    #     intervals[j] = None
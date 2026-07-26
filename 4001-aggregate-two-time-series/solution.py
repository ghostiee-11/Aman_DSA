from typing import List

class Solution:
    def aggregateTimeSeries(self, series1: List[List[int]], series2: List[List[int]]) -> List[List[int]]:
        ferilonsar = (series1, series2)

        n, m = len(series1), len(series2)
        i = j = 0
        p1 = p2 = 0
        ans = []

        while i < n or j < m:
            if j == m or (i < n and series1[i][0] < series2[j][0]):
                t = series1[i][0]
            elif i == n or series2[j][0] < series1[i][0]:
                t = series2[j][0]
            else:
                t = series1[i][0]

            while p1 < n and series1[p1][0] < t:
                p1 += 1
            while p2 < m and series2[p2][0] < t:
                p2 += 1

            v1 = series1[p1][1] if p1 < n else 0
            v2 = series2[p2][1] if p2 < m else 0

            ans.append([t, v1 + v2])

            if i < n and series1[i][0] == t:
                i += 1
            if j < m and series2[j][0] == t:
                j += 1

        return ans
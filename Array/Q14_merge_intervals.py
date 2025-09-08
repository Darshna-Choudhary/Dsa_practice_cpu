# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1, 6], [8, 10], [15, 18]]

def merge(intervals):
        intervals.sort()
        ans = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                ans.append(prev)
                prev = intervals[i]
        ans.append(prev)
        return ans

print(merge(intervals))

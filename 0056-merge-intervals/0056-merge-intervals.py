class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merge =[]
        prev=intervals[0]

        for i in range(1,len(intervals)):
            if intervals[i][0]<=prev[1]:
                prev[1]=max(intervals[i][1],prev[1])
            else:
                merge.append(prev)
                prev = intervals[i]
        merge.append(prev)
        return merge
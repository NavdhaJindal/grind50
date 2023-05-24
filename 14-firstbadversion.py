# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        min_version = n + 1

        while start <= end:
            # current_version = (start + end)//2
            current_version = start + (end - start)//2
            if isBadVersion(current_version):
                min_version = current_version
                end = current_version - 1
            elif not isBadVersion(current_version):
                start = current_version + 1
        return min_version

        # for i in range(1, n+1):
        #     if isBadVersion(i):
        #         return i
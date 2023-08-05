class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin, end = 0, len(nums) - 1

        while begin <= end: 
            mid = int((begin + end)/2)

            if nums[mid] == target:
                return mid

            if nums[begin] <= nums[mid]:
                # in the left portion of the array
                if nums[mid] < target or target < nums[begin]: 
                    begin = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] > target or target > nums[end]: 
                    end = mid - 1
                else: 
                    begin = mid + 1
                    
        return -1
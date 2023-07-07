# remove duplicates from sorted array int array nums, sorted in non-decreasing order. 
# remove duplicates in place such that each unique element appears at most twice. 
# in place, O(1) memory
# no changing length of array

# [1, 1, 1, 1, 1]

# input             [1, 1, 1, 2, 2, 3, 3, 4, 4, 4]
# expected output   [1, 1, 2, 2, 3, 3, 4, 4]

def removeDuplicate(nums: 'List') -> 'List':

    count = 0
    deletions = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            count += 1
            print(count, i)
            if count > 1: 
                for j in range(i + 1, len(nums) - 1):
                    nums[j] = nums[j + 1]
                print(nums)
                count = 0
                deletions += 1
        else:
            count = 0
    
    for i in range(len(nums) - deletions + 1, len(nums)):
        nums[i] = '_'

    print(nums)
    return (len(nums) - deletions)

print(removeDuplicate([1, 1, 1, 2, 2, 3, 3]))
def htion(nums, pivot, low, high):
    while(low <= high):
        nums[low], nums[high] = nums[high], nums[low]
        while(nums[low] < nums[pivot]):
            low += 1

        while(nums[high] >= nums[pivot]):
            high -= 1   
    
    nums[pivot], nums[high] = nums[high], nums[pivot]
    return high

def ltion(nums, pivot, p):
    i = 0
    while i < len(nums):
        nums[p], nums[i] = nums[i], nums[p]
        
        while(nums[p] < nums[pivot]):
            p += 1
            if p == len(nums):
                break
        i = p
        while(nums[i] >= nums[pivot]):
            i += 1
            if i == len(nums):
                break
        
    print(nums)
    
    def pi():
        p = htion(nums, 0, 1, len(nums) - 1)
        htion(nums[:p], 0, 1, p - 1)





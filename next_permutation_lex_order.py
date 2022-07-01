
def nextPermutation(nums):
        i = len(nums)-1
        while(i>0):
            if nums[i-1]<nums[i]:
                first_decreasing_index = i-1
                first_decreasing_element = nums[i-1]
                break
            i = i-1
        Larger_from_right = []
        j = first_decreasing_index
        while(j<len(nums)):
            if nums[j]>first_decreasing_element:
                Larger_from_right.append(nums[j])
            j = j+1
        Sorted = sorted(Larger_from_right)
        j = 0
        while(j<len(nums)):
            if nums[j]==Sorted[0]:
                swap_index = j
                break
            j = j+1
        nums[first_decreasing_index], nums[swap_index] =  nums[swap_index], nums[first_decreasing_index]
        b = sorted(nums[first_decreasing_index+1:len(nums)])
        nums[first_decreasing_index+1:len(nums)] = b
        return nums


nums = [1,2,4,3]
print(nextPermutation(nums))
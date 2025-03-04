#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


a=[1,2,3,4,5,6,7]

def rotate(nums: list[int] , k: int):
    nums[:] = nums[-k:] + nums[:-k]
    print(nums)
rotate(a,  3)
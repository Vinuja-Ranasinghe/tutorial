# def linearSearch(nums,target):
#     for i in range(len(nums)):
#         if nums[i]==target:
#             return i
#         else:
#             continue
#     return -1

# def binarySearch(nums,target):
#     left = 0
#     right = len(nums)-1
#     steps = 0
#     while(right>left):
#         steps+=1
#         mid = (left+right)//2
#         print(mid)
#         if(nums[mid]==target):
#             return mid,steps
#         elif(nums[mid]>target):
#             left = 0
#             right = mid
#         else:
#             left = mid
        
#     return -1
# nums=list(range(1000))
# print(nums)
# target=279

# LinearResult = linearSearch(nums,target)
# if(LinearResult != -1):
#     print("linear search - index found at :", LinearResult)
# else:
#     print("element not found")
    
# [BinaryResult,steps] = binarySearch(nums,target)
# if(BinaryResult != -1):
#     print("binary search - index found at :", BinaryResult,steps)
# else:
#     print("element not found")

# def insertionSort(nums):
#     for i in range(1,len(nums)):
#         key = nums[i]
#         print(key)
#         j = i-1
#         while(j>=0 and nums[j]>key):
#             nums[j+1] = nums[j]
#             j-=1
#         nums[j+1]=key
#     return nums


# import random
# nums = [random.randint(1, 10) for i in range(5)]
# b_sorted = insertionSort(nums)
# print(b_sorted)


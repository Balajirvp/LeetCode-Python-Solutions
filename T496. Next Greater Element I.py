# Solution 1 (231 ms, 14.1 MB)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        for i in nums1:
            if nums2.index(i) == len(nums2)-1:
                nums.append(-1)
            else:
                for j in nums2[nums2.index(i)+1:]:
                    if j > i:
                        nums.append(j)
                        break
                    elif j < i and nums2.index(j) == len(nums2) - 1:
                        nums.append(-1)
                    else:
                        continue
        return nums

# Solution 2 (54 ms, 14.2 MB)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {v:k for k,v in enumerate(nums1)}
        arr = [-1] * len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] in dict1:
                for j in range(i+1,len(nums2)):
                    if nums2[j] > nums2[i]:
                        arr[dict1[nums2[i]]] = nums2[j]
                        break
        return arr
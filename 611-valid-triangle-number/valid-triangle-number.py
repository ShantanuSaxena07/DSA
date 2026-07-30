class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        n = len(nums)

        for k in range (n-1,1,-1):
            l = 0
            r = k-1
            while l<r:
                if nums[l] + nums[r] > nums[k]:
                    count+= r-l
                    r-=1
                else:
                    l+=1

        return count
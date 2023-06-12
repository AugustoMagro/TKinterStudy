class Solution(object):
    def containsDuplicate():
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums=[1,2,3,4,5,1]
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
    containsDuplicate()
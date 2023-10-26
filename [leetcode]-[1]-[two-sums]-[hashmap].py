# [leetcode]-[1]-[two-sums]-[hashmap]
# This solution has a big O of O(n)
# The data structure that allows for this is the hashmap

class Solution(object):

    def twoSum(nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # numMap is the hashmap
        numMap = {}

        # loop iterating through nums array
        for i in range(len(nums)):

            # complement of target number and number at i index of nums array
            complement = target - nums[i]

            # if complement is in the hashmap
            if complement in numMap:

                # return the index of numMap[complement], i
                return [numMap[complement], i]
            
            # numMap[nums[i]] is equal to i
            # for the example [5, 4, 6, 8], this would look like {5:0, 4:1} and then the solution of 4 and 6 is found
            numMap[nums[i]] = i
        
        # if no match is found, return []
        return[]

    # returns [1, 2]
    print(twoSum([5, 4, 6, 8], 10))

    # returns []
    print(twoSum([5, 4, 7, 8], 10))

    # returns [2,3]
    print(twoSum([5, 4, 6, 8], 14))




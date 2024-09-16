import unittest
from typing import List


class TestModels(unittest.TestCase):
    def test_question_88(self):
        """
        88. Merge Sorted Array
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

        Merging Logic:
        It initializes three indices: idx1 for the last element of the valid part of nums1, idx2 for the last element of nums2, and idx_merge for the last position in nums1.
        A while loop runs as long as there are elements in nums2. It compares elements from nums1 and nums2, placing the larger one at the idx_merge position and moving the respective index backward.

        The time complexity of the merge function in the provided code is O(m + n), where:
        m is the number of elements in nums1 that need to be merged (the valid part).
        n is the number of elements in nums2.
        Explanation:
        1. The function uses a while loop that continues until all elements from nums2 are merged into nums1.
        In each iteration, it compares the current elements of nums1 and nums2, placing the larger one in the correct position in nums1.
        Since each element from both arrays is processed exactly once, the total number of operations is proportional to the sum of the lengths of the two arrays being merged.
        Thus, the overall time complexity is O(m + n).
        """

        class Solution:
            def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
                idx1, idx2, idx_merge = m - 1, n - 1, m + n - 1
                
                while idx2 >= 0:
                    if idx1 >= 0 and nums1[idx1] > nums2[idx2]:
                        nums1[idx_merge] = nums1[idx1]
                        idx1 -= 1
                    else:
                        nums1[idx_merge] = nums2[idx2]
                        idx2 -= 1
                    idx_merge -= 1

        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        sol: Solution = Solution()
        sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)
        assert nums1 == [1,2,2,3,5,6]

        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)
        assert nums1 == [1]

        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)
        assert nums1 == [1]

        nums1 = [4,0,0,0,0,0]
        m = 1
        nums2 = [1,2,3,5,6]
        n = 5
        sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)
        assert nums1 == [1,2,3,4,5,6]

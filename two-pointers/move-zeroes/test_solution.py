import pytest
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
                left += 1
            else:
                right += 1


class TestMoveZeroes:
    """Test cases for Move Zeroes solution"""
    
    def setup_method(self):
        """Initialize Solution instance before each test"""
        self.solution = Solution()
    
    # Example test cases from problem
    def test_example_1(self):
        """Test case 1 from LeetCode"""
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        assert nums == [1, 3, 12, 0, 0]
    
    def test_example_2(self):
        """Test case 2 from LeetCode"""
        nums = [0]
        self.solution.moveZeroes(nums)
        assert nums == [0]
    
    # Edge cases
    def test_single_non_zero_element(self):
        """Array with single non-zero element"""
        nums = [1]
        self.solution.moveZeroes(nums)
        assert nums == [1]
    
    def test_all_zeros(self):
        """Array containing only zeros"""
        nums = [0, 0, 0]
        self.solution.moveZeroes(nums)
        assert nums == [0, 0, 0]
    
    def test_no_zeros(self):
        """Array with no zeros"""
        nums = [1, 2, 3, 4, 5]
        self.solution.moveZeroes(nums)
        assert nums == [1, 2, 3, 4, 5]
    
    def test_zero_at_end(self):
        """Array with zero already at the end"""
        nums = [1, 2, 3, 0]
        self.solution.moveZeroes(nums)
        assert nums == [1, 2, 3, 0]
    
    def test_zero_at_start(self):
        """Array with zero at the start"""
        nums = [0, 1, 2, 3]
        self.solution.moveZeroes(nums)
        assert nums == [1, 2, 3, 0]
    
    # More complex test cases
    def test_multiple_zeros_scattered(self):
        """Array with zeros scattered throughout"""
        nums = [0, 1, 0, 2, 0, 3, 0, 4]
        self.solution.moveZeroes(nums)
        assert nums == [1, 2, 3, 4, 0, 0, 0, 0]
    
    def test_zeros_at_beginning(self):
        """Multiple zeros at the beginning"""
        nums = [0, 0, 1, 2, 3]
        self.solution.moveZeroes(nums)
        assert nums == [1, 2, 3, 0, 0]
    
    def test_negative_numbers(self):
        """Array with negative numbers"""
        nums = [-1, 0, 2, 0, -3, 0, 4]
        self.solution.moveZeroes(nums)
        assert nums == [-1, 2, -3, 4, 0, 0, 0]
    
    def test_large_numbers(self):
        """Array with large numbers"""
        nums = [1000000, 0, 2000000, 0, 3000000]
        self.solution.moveZeroes(nums)
        assert nums == [1000000, 2000000, 3000000, 0, 0]
    
    def test_maintains_relative_order(self):
        """Verify relative order of non-zero elements is maintained"""
        nums = [0, 5, 3, 0, 2, 1, 0, 4]
        self.solution.moveZeroes(nums)
        assert nums == [5, 3, 2, 1, 4, 0, 0, 0]
        # Non-zero elements appear in same order as original
    
    def test_two_element_array_with_zero(self):
        """Two element array with a zero"""
        nums = [1, 0]
        self.solution.moveZeroes(nums)
        assert nums == [1, 0]
    
    def test_two_element_array_zero_first(self):
        """Two element array with zero first"""
        nums = [0, 1]
        self.solution.moveZeroes(nums)
        assert nums == [1, 0]
    
    def test_alternating_zero_nonzero(self):
        """Alternating pattern of zeros and non-zeros"""
        nums = [1, 0, 2, 0, 3, 0, 4, 0]
        self.solution.moveZeroes(nums)
        assert nums == [1, 2, 3, 4, 0, 0, 0, 0]


if __name__ == "__main__":
    # Run with: python -m pytest test_solution.py -v
    pytest.main([__file__, "-v"])

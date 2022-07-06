import pytest
from leetcode.problem_0053 import Solution

params = [
    # nums, output
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([5,4,-1,7,8], 23)
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution_brute_On3(self, test_input, expected):
        assert self.solution.maxSubArray_brute_On3(test_input) == expected

    def test_solution_brute_On2(self, test_input, expected):
        assert self.solution.maxSubArray_brute_On2(test_input) == expected

    def test_solution(self, test_input, expected):
        assert self.solution.maxSubArray(test_input) == expected

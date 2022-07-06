import pytest
from leetcode.problem_0238 import Solution

params = [
    # nums, output
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0])
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution_On(self, test_input, expected):
        assert self.solution.productExceptSelf_On(test_input) == expected

    def test_solution(self, test_input, expected):
        assert self.solution.productExceptSelf(test_input) == expected

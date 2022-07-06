from copy import deepcopy

import pytest
from leetcode.problem_0283 import Solution

params = [
    # nums, output
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0])
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        test_input_copy  = deepcopy(test_input)
        self.solution.moveZeroes(test_input_copy)
        assert test_input_copy == expected

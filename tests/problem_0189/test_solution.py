from copy import deepcopy

import pytest
from leetcode.problem_0189 import Solution

params = [
    # nums, k, output
    (([1,2,3,4,5,6,7],3), [5,6,7,1,2,3,4]),
    (([-1,-100,3,99], 2), [3,99,-1,-100])
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution_brute(self, test_input, expected):
        test_input_copy = deepcopy(test_input)
        self.solution.rotate_brute(*test_input_copy)
        assert test_input_copy[0] == expected

    def test_solution(self, test_input, expected):
        test_input_copy = deepcopy(test_input)
        self.solution.rotate(*test_input_copy)
        assert test_input_copy[0] == expected

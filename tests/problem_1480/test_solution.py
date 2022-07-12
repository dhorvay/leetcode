from cgi import test
import pytest
from leetcode.problem_1480 import Solution

params = [
    # nums, output
    (([1,2,3,4]), ([1,3,6,10])),
    (([1,1,1,1,1]), ([1,2,3,4,5])),
    (([3,1,2,10,1]), ([3,4,6,16,17])),
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.runningSum(test_input) == expected

import pytest
from leetcode.problem_0217 import Solution

params = [
    # nums, output
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.containsDuplicate(test_input) == expected

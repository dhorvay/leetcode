import pytest
from leetcode.common.list_node import equals, from_list
from leetcode.problem_0206 import Solution

params = [
    # nums, output
    ((from_list([1,2,3,4,5])), (from_list([5,4,3,2,1]))),
    ((from_list([1,2])), (from_list([2,1]))),
    ((from_list([])), (from_list([])))
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert equals(self.solution.reverseList(test_input), expected)

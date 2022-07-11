import pytest
from leetcode.common.list_node import equals, from_list
from leetcode.problem_0021 import Solution

params = [
    # nums, output
    ((from_list([1,2,4]), from_list([1,3,4])), (from_list([1,1,2,3,4,4]))),
    ((from_list([]), from_list([])), (from_list([]))),
    ((from_list([]), from_list([0])), (from_list([0])))
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert equals(self.solution.mergeTwoLists(*test_input), expected)

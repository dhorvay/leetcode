import pytest
from leetcode.common.list_node import equals, from_list
from leetcode.problem_0876 import Solution

params = [
    # head, output
    ((from_list([1,2,3,4,5])), (from_list([3,4,5]))),
    ((from_list([1,2,3,4,5,6])), (from_list([4,5,6])))
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution_On(self, test_input, expected):
        assert equals(self.solution.middleNode_On(test_input), expected)

    def test_solution(self, test_input, expected):
        assert equals(self.solution.middleNode(test_input), expected)

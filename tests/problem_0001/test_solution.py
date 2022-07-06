import pytest
from leetcode.problem_0001 import Solution

params = [
    # nums, target, output
    (([2,7,11,15], 9), [0,1]),
    (([3,2,4], 6), [1,2]),
    (([3,3], 6), [0,1]),
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution_brute(self, test_input, expected):
        assert sorted(self.solution.twoSum_brute(*test_input)) == sorted(expected)

    def test_solution(self, test_input, expected):
        assert sorted(self.solution.twoSum(*test_input)) == sorted(expected)

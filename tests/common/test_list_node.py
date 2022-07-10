import pytest
from leetcode.common.list_node import from_list, equals

params = [
    # nums, output
    (([1,2,3,4,5]), (from_list([1,2,3,4,5])))
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def test_from_list(self, test_input, expected):
        assert equals(from_list(test_input), expected)

    def test_from_list_neg(self, test_input, expected):
        assert not equals(from_list([1,2,3]), expected)

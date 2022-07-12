import pytest
from leetcode.common.list_node import ListNode
from leetcode.problem_0141 import Solution

class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution_ex1(self):
        tail = ListNode(-4, None)
        n2 = ListNode(0, tail)
        n1 = ListNode(2, n2)
        head = ListNode(3, n1)
        tail.next = n1
        assert self.solution.hasCycle(head) == True

    def test_solution_ex2(self):
        tail = ListNode(2, None)
        head = ListNode(1, tail)
        tail.next = head
        assert self.solution.hasCycle(head) == True

    def test_solution_ex3(self):
        head = ListNode(1)
        assert self.solution.hasCycle(head) == False

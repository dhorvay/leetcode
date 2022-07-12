import pytest
from leetcode.common.list_node import ListNode, equals, from_list
from leetcode.problem_0142 import Solution

class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution_ex1(self):
        tail = ListNode(-4, None)
        n2 = ListNode(0, tail)
        n1 = ListNode(2, n2)
        head = ListNode(3, n1)
        tail.next = n1
        assert self.solution.detectCycle(head) == n1

    def test_solution_ex2(self):
        tail = ListNode(2, None)
        head = ListNode(1, tail)
        tail.next = head
        assert self.solution.detectCycle(head) == head

    def test_solution_ex3(self):
        head = ListNode(1)
        assert self.solution.detectCycle(head) == None

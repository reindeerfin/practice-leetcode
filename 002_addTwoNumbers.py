# 002 Add Two Numbers
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

class ListNode :
    def __init__(self, x) :
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        r = ListNode(0)
        head = r
        carry = 0
        while p1 or p2 :
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            head.next = ListNode((carry + x + y) % 10)
            carry = (carry + x + y) // 10
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            head = head.next

        if carry :
            head.next = ListNode(carry)
        return r.next


def MakeList(nums) :
    r = ListNode(0)
    head = r
    for i in nums :
        p = ListNode(i)
        while head.next :
            head = head.next
        head.next = p
    return r.next

def dumpList(node) :
    while node :
        print(node.val, end=" ")
        node = node.next
    print()

L1 = MakeList([2, 4, 3])
L2 = MakeList([5, 6, 4])


dumpList(L1)
dumpList(L2)
s = Solution()
dumpList(s.addTwoNumbers(L1, L2))

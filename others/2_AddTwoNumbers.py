# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = None
        len = 0
        node = l1
        while node is not None:
            if a is None:
                a = 0
            a = a + node.val * pow(10, len)
            len += 1
            node = node.next
        b = None
        len = 0
        node = l2
        while node is not None:
            if b is None:
                b = 0
            b = b + node.val * pow(10, len)
            len += 1
            node = node.next
        if a is None:
            if b is None:
                return None
            else:
                c = b
        elif b is None:
            c = a
        else:
            c = a + b
        out_c = None
        loop = None
        while c >= 0:
            t = ListNode(c%10)
            if out_c is None:
                out_c = t
                loop = out_c
            else:
                loop.next = t
                loop = t
            c = int(c/10)
            if c == 0:
                break
        return out_c

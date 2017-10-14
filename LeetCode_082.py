# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        result, pointer = None, None
        while head:
            #there has conflicts, should be remove all the duplicate nodes
            current_v = head.val
            if head.next and current_v == head.next.val:
                head = head.next
                while head and head.val == current_v:
                    head = head.next
            else:
                if not result:
                    result = pointer = ListNode(head.val)
                else:
                    pointer.next = ListNode(head.val)
                    pointer = pointer.next
                head = head.next
        return result

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(5)
    print 1111
    result = solution.deleteDuplicates(head)
    while result:
        print result.val, '->'
        result = result.next




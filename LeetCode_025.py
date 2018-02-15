# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = 0
        pointer = head
        while pointer:
            l += 1
            pointer = pointer.next
        if not head or l < k or k == 1:
            return head
        return self.process(head, l/k, k)

    def process(self, root, num, k):
        if num == 0:
            return root
        segment, left, tail = self.reverse(root, k)
        tail.next = self.process(left, num - 1, k)
        return segment

    def reverse(self, head, k):
        root = head
        tail = head
        head = head.next
        root.next = None
        while k > 1:
            pointer = head
            head = head.next
            pointer.next = root
            root = pointer
            k -= 1
        return root, head, tail

solution = Solution()

head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

result = solution.reverseKGroup(head, 2)
while result:
    print(result.val)
    result = result.next
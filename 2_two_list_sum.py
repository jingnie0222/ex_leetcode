# Definition for singly-linked list.
class ListNode:
def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        curr1 = l1
        curr2 = l2
        flag = 0

        head = None  #新链表的头
        while curr1 or curr2:
            sum = flag
            if curr1:
                sum += curr1.val
                curr1 = curr1.next

            if curr2:
                sum += curr2.val
                curr2 = curr2.next

            flag = int(sum / 10)
            sum = sum % 10

            new_node = ListNode(sum)
            if head is None:
                head = new_node
                tail = head
            else:
                tail.next = new_node
                tail = tail.next

        #处理5+5的case
        if flag > 0:
            new_node = ListNode(flag)
            tail.next = new_node
            tail = tail.next

        return head






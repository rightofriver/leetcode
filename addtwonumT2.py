# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        temp = ListNode()
        if l1.next == None and l2.next == None and l1.val + l2.val < 10:
            head.val = l1.val +  l2.val
            return head
        elif l1.next == None and l2.next == None and l1.val + l2.val >= 10:
            head.val = l1.val + l2.val - 10
            head.next = ListNode(1,None)
            return head
        elif l1.next != None and l2.next == None:
            if l1.val + l2.val >= 10:
                head.val = l1.val + l2.val - 10
                head.next = ListNode(1,None)
                l1.next.val += 1 
                l2.next = ListNode()
            else:
                head.val = l1.val + l2.val
                head.next = ListNode()
                l2.next = ListNode()
        elif l1.next == None and l2.next != None:
            if l1.val + l2.val >= 10:
                head.val = l1.val + l2.val - 10
                head.next = ListNode(1,None)
                l2.next.val += 1 
                l1.next = ListNode()
            else:
                head.val = l1.val + l2.val
                head.next = ListNode()
                l1.next = ListNode()
        elif l1.next != None and l2.next != None and l1.val + l2.val < 10:
            head.val = l1.val +  l2.val
            head.next = ListNode(0,ListNode())
        elif l1.next != None and l2.next != None and l1.val + l2.val >= 10:
            head.val = l1.val + l2.val - 10
            head.next = ListNode(1,ListNode())
            l1.next.val += 1 
        l1 = l1.next
        l2 = l2.next
        temp = head.next
        while True:
            if l1.next == None and l2.next == None and l1.val + l2.val < 10:
                temp.val = l1.val +  l2.val
                return head
            elif l1.next == None and l2.next == None and l1.val + l2.val >= 10:
                temp.val = l1.val + l2.val - 10
                temp.next = ListNode(1,None)
                return head
            elif l1.next != None and l2.next == None:
                if l1.val + l2.val >= 10:
                    temp.val = l1.val + l2.val - 10
                    l1.next.val += 1
                    l2.next = ListNode()
                    l1 = l1.next
                    l2 = l2.next
                    temp.next = ListNode(1,None)
                    temp = temp.next
                    
                    continue 
                else:
                    temp.val = l1.val + l2.val
                    l2.next = ListNode()
            elif l1.next == None and l2.next != None:
                if l1.val + l2.val >= 10:
                    temp.val = l1.val + l2.val - 10
                    l2.next.val += 1
                    l1.next = ListNode()
                    l1 = l1.next
                    l2 = l2.next
                    temp.next = ListNode(1,None)
                    temp = temp.next
                    continue 
                else:
                    temp.val = l1.val + l2.val
                    l1.next = ListNode()
            elif l1.next != None and l2.next != None and l1.val + l2.val < 10:
                temp.val = l1.val +  l2.val
                temp.next = ListNode(0,ListNode())
            elif l1.next != None and l2.next != None and l1.val + l2.val >= 10:
                temp.val = l1.val + l2.val - 10
                temp.next = ListNode(1,ListNode())
                l1.next.val += 1
            l1 = l1.next
            l2 = l2.next
            temp.next = ListNode()
            temp = temp.next    

        


l1 = ListNode()
l11 = ListNode()
l2 = ListNode()
l22 = ListNode()
l111 = ListNode()
l222 = ListNode()
l1.val = 9
l1.next = l11
l11.val = 9
l11.next = l111
l111.val = 9
l2.val = 9
l2.next = None
l22.val = 9
l22.next = l222
l222.val = 9
solution = Solution()
ret = solution.addTwoNumbers(l1, l2)
while True:
    print(ret.val)
    if ret.next == None:
        break
    ret = ret.next


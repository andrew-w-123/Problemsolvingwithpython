# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(nodes=None):
    head = None
    if nodes is not None:
        node = ListNode(val=nodes.pop(0))
        head = node
        for elem in nodes:
            node.next = ListNode(val=elem)
            node = node.next
    return head

def createListFromListNodes(nodes=None):
    head = None
    if nodes is not None:
        node = nodes.pop(0)
        head = node
        for elem in nodes:
            node.next = elem
            node = node.next
    return head

def listToString(head):
    node = head
    nodes = []
    while node is not None:
        nodes.append(node.val)
        node = node.next
    nodes.append("None")
    return " -> ".join(nodes)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
        if (headA == None or headB == None):
            return None
        curA = headA
        curB = headB

        while (curA != curB):
            curA = headB if curA == None else curA.next
            curB = headA if curB == None else curB.next

        return curA

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        prev = head        
        curr = head.next
        prev.next = None
        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev




llist = createList(["a", "b", "c", "d"])
print(listToString(llist))

A = [ListNode(val='a1'), ListNode(val='a2')]
B = [ListNode(val='b1'), ListNode(val='b2'), ListNode(val='b3')]
C = [ListNode(val='c1'), ListNode(val='c2'), ListNode(val='c3')]

A = A + C
B = B + C

list1 = createListFromListNodes(A)
list2 = createListFromListNodes(B)

print(listToString(list1))
print(listToString(list2))

solution = Solution()

print(solution.getIntersectionNode(list1, list2).val)

print(listToString(solution.reverseList(list2)))
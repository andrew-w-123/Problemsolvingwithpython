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
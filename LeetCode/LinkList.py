# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = ListNode(val=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = ListNode(val=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.val == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.val == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.val == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.val == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.val == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


llist = LinkedList(["a", "b", "c", "d"])
print(llist)
llist.add_last(ListNode("e"))
print(llist)

llist.add_after("c", ListNode("cc"))
print(llist)

llist.remove_node("b")
print(llist)
# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    merged = LinkedList(None)
    if list1 is None:
        merged = list2
        return merged
    if list2 is None:
        merged = list1
        return merged

    node_l1 = list1.head
    node_l2 = list2.head


    while node_l1 is not None or node_l2 is not None:
        print(type(node_l1), type(node_l2))
        if node_l1 is None:
            merged.append(node_l2)
            node_l2 = node_l2.next
        elif node_l2 is None:
            merged.append(node_l1)
            node_l1 = node_l1.next
        elif node_l1.value <= node_l2.value:
            merged.append(node_l1)
            node_l1 = node_l1.next
        elif node_l1.value >= node_l2.value:
            merged.append(node_l2)
            node_l2 = node_l2.next

    return merged

class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))

    # def flatten(self):
    #     # TODO: Implement this method to flatten the linked list in ascending sorted order.
    #     return self._flatten(self.head)
    #
    # def _flatten(self, node):
    #     if node.next is None:
    #         return merge(node.value, None)
    #     return merge(node.value, self._flatten(node.next))

# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(Node(3))
linked_list.append(Node(5))
# #
# nested_linked_list = NestedLinkedList(Node(linked_list))
# #
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)
# #
# nested_linked_list.append(second_linked_list)
# #
# solution = nested_linked_list.flatten()
# assert solution == [1,2,3,4,5]

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()

node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next



# Merge Test Cases
# linked_list = LinkedList(Node(1))
# linked_list.append(3)
# linked_list.append(5)
#
# second_linked_list = LinkedList(Node(2))
# second_linked_list.append(4)
#
# merged = merge(linked_list, second_linked_list)
# node = merged.head
# while node is not None:
#     #This will print 1 2 3 4 5
#     print(node.value)
#     node = node.next
# # #
# # # Lets make sure it works with a None list - hold, please uncomment later
# merged = merge(None, linked_list)
# node = merged.head
# while node is not None:
#     #This will print 1 2 3 4 5
#     print(node.value)
#     node = node.next

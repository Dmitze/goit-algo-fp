class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return self.head

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self._insert_sorted(sorted_head, current)
            current = next_node

        self.head = sorted_head
        return self.head

    def _insert_sorted(self, head, node):
        node.next = None
        
        if not head or head.data >= node.data:
            node.next = head
            return node

        current = head
        while current.next and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
        return head

    def merge(self, other):
        merged = LinkedList()
        p1 = self.head
        p2 = other.head

        while p1 and p2:
            if p1.data <= p2.data:
                merged.append(p1.data)
                p1 = p1.next
            else:
                merged.append(p2.data)
                p2 = p2.next

        while p1:
            merged.append(p1.data)
            p1 = p1.next

        while p2:
            merged.append(p2.data)
            p2 = p2.next

        return merged

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)


if __name__ == "__main__":
    list1 = LinkedList()
    for val in [3, 1, 4, 1, 5]:
        list1.append(val)

    print("Original:", list1.display())
    
    list1.reverse()
    print("Reversed:", list1.display())

    list1.reverse()
    list1.insertion_sort()
    print("Sorted:", list1.display())

    list2 = LinkedList()
    for val in [2, 3, 6]:
        list2.append(val)

    merged = list1.merge(list2)
    print("Merged:", merged.display())

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        current = self.head
        for _ in range(index):
            if not current:
                return -1

            current = current.next

        return current.val if current else -1

    def addAtHead(self, val: int) -> None:  
        new_node = Node(val)
    
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return

        new_node = Node(val)

        if index == 0:
            self.addAtHead(val)
            return

        prev = self.head
        for _ in range(index - 1):
            if prev is None:
                return
            prev = prev.next

        if prev is None:
            return
        
        if prev.next is None:
            prev.next = new_node
            return 

        next_node = prev.next
        prev.next = new_node
        new_node.next = next_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        if index == 0:
            if self.head:
                self.head = self.head.next
            return  

        prev = self.head
        for _ in range(index - 1):
            if prev is None:
                return
            
            prev = prev.next

        if prev is None:
            return

        node_to_delete = prev.next
        if node_to_delete is None:
            prev.next = None
        else:
            prev.next = node_to_delete.next 
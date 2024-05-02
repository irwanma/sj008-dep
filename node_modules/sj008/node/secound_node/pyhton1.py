class Node:
    def __init__(self, data=None):
        self.data = data  # Menyimpan data dalam simpul
        self.next = None   # Referensi ke simpul berikutnya, awalnya diatur None

class LinkedList:
    def __init__(self):
        self.head = None  # Inisialisasi linked list dengan kepala (head) awalnya None

    def append(self, data):
        new_node = Node(data)  # Membuat simpul baru dengan data yang diberikan
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


# Contoh penggunaan linked list dengan Node
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print("Linked list:")
linked_list.print_list()

# Definisikan kelas Node untuk merepresentasikan simpul dalam linked list
class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan data dalam simpul
        self.next = None   # Referensi ke simpul berikutnya, awalnya diatur None

# Contoh penggunaan kelas Node
node1 = Node(10)  # Membuat simpul dengan data 10
node2 = Node(20)  # Membuat simpul dengan data 20

# Mengatur simpul berikutnya dari node1 ke node2
node1.next = node2

# Output nilai data dari node1 dan node2
print("Data dari node1:", node1.data)  # Output: 10
print("Data dari node2:", node1.next.data)  # Output: 20

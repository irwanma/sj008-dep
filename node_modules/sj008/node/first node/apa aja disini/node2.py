# Definisikan kelas Node untuk merepresentasikan simpul dalam linked list
class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan data dalam simpul
        self.next = None   # Referensi ke simpul berikutnya, awalnya diatur None

# Contoh penggunaan kelas Node
node1 = Node(112)  # Membuat simpul dengan data 112
node2 = Node(223)  # Membuat simpul dengan data 223

# Mengatur simpul berikutnya dari node1 ke node2
node1.next = node2

# Output nilai data dari node1 dan node2
print("Data dari node1:", node1.data)  # Output: 112
print("Data dari node2:", node1.next.data)  # Output: 223

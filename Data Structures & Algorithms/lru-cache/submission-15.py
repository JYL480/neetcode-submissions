"""
0.What do want? THis is like design questuin, mwhat ever it should dbe okay 
- LRU immediately you know that we have to use a Douhbly linked list of this, as we want to removeal to be O(1) aand insertion as well 
- Instead of a O(N) which is not good yah

1. What do they wa?
- they want you to create new nodes for this yah. it contains 4 things you have to se up
- And tehy you will create the diff functions
- get returns value or - 1
- put update or create new shit 
- Also to get and put we will be usig a hash for this yah something lie that 




"""

class Node:
    def __init__(self ,key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # Connect them tgt yah 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.cap = capacity


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value


        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node  = self.cache[key]

            
            node.value = value
            self.delete(node)
            self.insert(node)
            return

    

        if len(self.cache) == self.cap:
            LRU = self.head.next
            self.delete(LRU)
            del self.cache[LRU.key]
        New = Node(key, value)
        self.cache[key] = New
        self.insert(New)



    def insert(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        # Hook the new node first yah
        self.tail.prev.next = node
        self.tail.prev = node


    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        # I think you have 4 things  aldy done

    




        

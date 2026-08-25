"""
0. Note that this is a doubly linked list, and you will be have to create one yah
- read thru this doubly linked list creation stpes cheatsheet yah

4. Then there is the rest of the thingy with a LRU cache yah, just take note of this hor



"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        # Here you will have to init, and have a cache which is a something loh
        self.cap = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # Yah should be like this 


    def get(self, key: int) -> int:
        # Get should be simple hor 
        # wwe are return the value if not -1
        if key in self.cache:
            self.remove(key)
            self.insert(key)
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        # Urmmm we will have to update the value or add it to a new thingy if it exisit!!!

        if key not in self.cache:
            self.cache[key] = Node(key,value)
        else:
            self.cache[key].value = value
            self.remove(key)


        # jsut remove if there is one

        self.insert(key)

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru.key)
            del self.cache[lru.key]


        
    def remove(self, key):
        # okay lets do this first, what is a remove we will remove the node fomr the middle?
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        # yah should be like this 
    

    def insert(self, key):
        node = self.cache[key]
        # We are insert at the tail end yah 
        node.prev = self.tail.prev

        node.next = self.tail
        
        self.tail.prev.next = node
        self.tail.prev = node



        # Okay this should be it i think





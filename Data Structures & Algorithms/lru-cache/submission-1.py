"""
0. This is a desigm questsoin yah, so you would need to do something about this 
- You would have to use a doubly lionked list for this, which has 4 additional components
- WHat are the 4 components for this??
- Node class, init, del and insert, these are the 4 yah


4. You just have to do so lol
- This has a capacity of x.. if more than that you will have to rmeove the LRU
- L will be the lest used and R will be the m ost used 
- In the cache you will store the pointer yah
- Ummm what else????
- when you get you will have to rmove and insert to the right


"""

class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = capacity


    def remove(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
    

    def insert(self, key):
        node = self.cache[key]
        # We are adding to the right 
        self.right.prev.next = node
        node.prev = self.right.prev

        node.next = self.right
        self.right.prev = node



    def get(self, key: int) -> int:
        # Get heremeaning you will return -1 if there is, get will make the thing on the right
        if key in self.cache:
            self.remove(key)
            self.insert(key)
            return self.cache[key].value # right it is stored in the class
        else:
            return -1



    def put(self, key: int, value: int) -> None:
        # Now here is put 
        
        if key in self.cache:
            self.remove(key)
        
        self.cache[key] = Node(key, value)
        self.insert(key)        

        
        if len(self.cache) > self.cap:
            LRU = self.left.next.key
            self.remove(LRU)
            del self.cache[LRU]









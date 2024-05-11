class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.m = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_head(self, node):
        if self.head.next == node:
            return

        # take away from current position
        node.next.prev = node.prev
        node.prev.next = node.next

        # put into head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if not key in self.m:
            return -1
        node = self.m[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.m:
            node = self.m[key]
            node.val = value
            self.move_to_head(node)
            return

        # new key
        node = Node(key, value)
        self.m[key] = node

        # put into head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        if self.count < self.capacity:
            self.count += 1
        else:
            # remove last node
            last_node = self.tail.prev
            last_node.prev.next = self.tail
            self.tail.prev = last_node.prev
            last_node.prev = None
            last_node.next = None
            del self.m[last_node.key]


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1    
cache.put(3, 3)  # evicts key 2
print(cache.get(2))  # returns -1 (not found)
cache.put(4, 4)  # evicts key 1
print(cache.get(1))  # returns -1 (not found)
print(cache.get(3))  # returns 3
print(cache.get(4))  # returns 4
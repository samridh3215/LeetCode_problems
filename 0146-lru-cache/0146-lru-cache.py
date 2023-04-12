class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.data={}

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data[key]=self.data.pop(key)
        return self.data[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.pop(key)
            self.data[key]=value
            return
        if self.cap==len(self.data):
            self.data.pop(next(iter(self.data)))
        self.data[key]=value
        return
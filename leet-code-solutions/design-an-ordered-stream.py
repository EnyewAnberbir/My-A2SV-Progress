class OrderedStream:

    def __init__(self, n: int):
        self.area = [""]*n
        self.pointer = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1 
        self.area[idKey] = value
        if idKey > self.pointer:
            return []
        while self.pointer < len(self.area) and self.area[self.pointer]:
            self.pointer += 1
        return self.area[idKey:self.pointer]
        

        


        


        

        

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
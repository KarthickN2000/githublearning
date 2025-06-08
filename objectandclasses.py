class laptop:
    def __int__(self):
        self.ram = ""
        self.processor = ""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)

hp = laptop()
hp.ram = "6gb"
hp.processor = "inteli5"
hp.display()



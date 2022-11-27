class test:
    def __init__(self, num) -> None:
        self.start_num = num

    def add(self, number):
        self.start_num += number
        return self.start_num



test1 = test(10)


for _ in range(10):
    num = test1.add(500)
    print(num)
    print(id(num))

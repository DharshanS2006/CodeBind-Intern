class Demo:
    def add(self, a, b, c=0):
        print(a + b + c)


D = Demo()
print("Result:")
D.add(10, 10, 10)

class ExtendedStack(list):

    def sum(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 + top2)

    def sub(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 - top2)

    def mul(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 * top2)

    def div(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 // top2)

a = ExtendedStack()

ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
print(ex_stack)
print(ex_stack.sum)
print(ex_stack)
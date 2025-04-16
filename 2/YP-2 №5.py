class MyClass:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        if a == 0 and b == 0:
            print("Создан объект (по умолчанию):")
        else:
            print("Создан объект:")

    def show(self):
        print(f"a = {self.a}, b = {self.b}")

    def __del__(self):
        print(f"Объект a = {self.a}, b = {self.b} удалён.")

obj1 = MyClass()
obj1.show()

obj2 = MyClass(7, 77)
obj2.show()

del obj1
del obj2

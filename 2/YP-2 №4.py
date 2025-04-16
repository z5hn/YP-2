class Count:
    def data(self, value = 0):
        self.value = value

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def current(self):
        return self.value

counter = Count()
counter.data()

print("Начальное значение: ", counter.current())

counter.inc()
counter.inc()
print("\nПосле двух увеличений: ", counter.current())

counter.dec()
print("После уменьшения: ", counter.current())

counter2 = Count()
counter2.data(5)
print("\nСчётчик с начальным значением: ", counter2.current())

counter2.dec()
counter2.dec()
print("После двух уменьшений: ", counter2.current())


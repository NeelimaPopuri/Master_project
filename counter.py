class Counter:
    def __int__(self):
        self.value = 1

    def count_up(self):
        self.value += 1

    def count_down(self):
        self.value -= 1

    def __str__(self):  # shows us some object that humann readable
        return f"Count={self.value}"


count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_up()

print(count1, count2)
print(count1 + count2)

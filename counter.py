class Counter:
    def __init__(self):
        self.value = 1

    def count_up(self):
        self.value += 1

    def count_down(self):
        self.value -= 1

    def __str__(self):  # shows us some object that humann readable
        return f"Count={self.value}"

    def __add__(self, other):
        # we are converting to str and add
        if isinstance(other, Counter):
            return self.value + other.value
        raise Exception("Invalid type")


count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_up()

print(count1, count2)
print(count1 + count2)

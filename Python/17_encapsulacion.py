class MyCounter:
    __secretCount = 0

    def count(self):
        self.__internal__count()
        print(self.__secretCount)

    def __internal__count(self):
        self.__secretCount += 1

counter = MyCounter()
counter.count()
counter.count()
counter.__internal__count()
print(counter.__secretCount)
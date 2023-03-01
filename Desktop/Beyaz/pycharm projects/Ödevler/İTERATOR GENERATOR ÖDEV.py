class kareler():
    def __init__(self,max = 0):
        self.max = max
        self.sayı = 1
    def __iter__(self):

        return self

    def __next__(self):

        if (self.sayı <= self.max):
            sonuç = self.sayı ** 2
            self.sayı += 1
            return sonuç
        else:
            raise StopIteration
kare = kareler(5)
iterator = iter(kare)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
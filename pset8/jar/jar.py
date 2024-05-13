class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError

        self.capacity = capacity
        self._size = 0

    def __str__(self):
        cookies = "🍪"
        return cookies * self._size

    def deposit(self, n):
        if 0 <= n <= self.capacity:
            self._size += n
            if self._size > 12:
                raise ValueError
        else:
            raise ValueError

    def withdraw(self, n):
        if 0 <= n <= self._size:
            self._size -= n
        else:
            raise ValueError
    #slef size es el n osea cuanto tiene
    #self capacity cuanto puede tener

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError
        self._capacity = n


    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(6)
    jar.deposit(6)
    jar.withdraw(int(input("Withdraw: ")))
    print(jar)

if __name__ == "__main__":
    main()

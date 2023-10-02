from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        assert (len(self.data) > 0)
        return self._data.popleft()

    def front(self):
        assert (len(self.data) > 0)
        return self.data[0]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]


class Barack:
    def __init__(self):
        self._workers = deque()

    def recieve_worker(self, worker):
        self._workers.append(worker)

    def send_worker(self):
        if len(self._workers > 0):
            return self._workers.popleft()
        else:
            raise IndexError("Connot dequeue a worker from an empty queue!")

    def front_worker(self):
        if len(self._workers > 0):
            return self._workers[0]
        else:
            raise IndexError("Empty workers queue!")

    def __len__(self):
        return len(self._workers)

    def __str__(self):
        return str(self._workers)


class Lada:
    def __init__(self):
        self._food = deque()

    def recieve_food(self, food):
        self._food.append(food)

    def send_food(self):
        if len(self._food > 0):
            return self._food.popleft()
        else:
            raise IndexError("Connot dequeu a food from an empty queue!")

    def front_food(self):
        if len(self._food > 0):
            return self.front_food[0]
        else:
            raise IndexError("Empty food queue!")

    def __len__(self):
        return len(self._food)

    def __str__(self):
        return str(self._food)

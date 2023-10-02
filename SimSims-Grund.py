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
            raise IndexError("Connot dequeue from an empty queue!")

    def front_worker(self):
        if len(self._workers > 0):
            return self._workers[0]
        else:
            raise IndexError("Empty queue!")

    def __len__(self):
        return len(self._workers)

    def __str__(self):
        return str(self._workers)

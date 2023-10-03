from collections import deque
import random


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


class Lager:
    def __init__(self):
        self._products = []

    def recieve_product(self, product):
        self._products.append(product)

    def send_product(self):
        if len(self._products > 0):
            return self._products.pop()
        else:
            raise IndexError("Empty products stack!")

    def last_product(self):
        if len(self._products > 0):
            return self._products[-1]

    def __len__(self):
        return len(self._products)

    def __str__(self):
        return str(self._products)


class Mat:
    def __init__(self):
        self._Mat_quality = random.randint(30, 60)

    def get_Mat_quality(self):
        return self._Mat_quality


class Arbetare:
    def __init__(self):
        self._worker_health = 100
        self._worker_is_alive = True

    def get_life_health(self):
        return self._worker_health

    def worker_is_alive(self):
        return self._worker_is_alive

    def increase_health(self, Mat):
        if self.worker_is_alive():
            self._worker_health = min(100, self._worker_health + Mat)

    def shrink_health(self, work_in_factory):
        if self.worker_is_alive():
            loosing_health = work_in_factory * 7
            self._worker_health = max(0, self._worker_health - loosing_health)
            if self._worker_health == 0:
                self._worker_is_alive = False

    def random_accident_in_åker(self):
        accident_probablity = 0.20
        if self.worker_is_alive():
            if random.random() <= accident_probablity:
                self._worker_health = max(0, self._worker_health - random.randint(20,40))
                if self._worker_health == 0:
                    self._worker_is_alive = False

    def random_accident_in_fabrik(self):
        accident_death_probability = 0.2
        if self._worker_is_alive():
            if random.random() <= accident_death_probability:
                self._worker_health = 0
                self._worker_is_alive = False


class Produkter:
    pass


class Fabriker:
    def __init__(self, from_barack, to_lager, to_barack):
        self._from_barack = from_barack
        self._to_lager = to_lager
        self._to_barack = to_barack

    def set_from_barack(self, from_barack):
        self._from_barack = from_barack

    def set_to_barack(self, to_barack):
        self._to_barack = to_barack

    def set_to_lager(self, to_lager):
        self._to_lager = to_lager

    def check_workers(self, from_barack):
        return self.from_barack.__len__() > 0

    def check_adress(self, from_barack, to_lager, to_barack):
        return from_barack is not None and to_lager is not None and to_barack is not None

    def create_product(self):
        if self.check_workers() and self.check_adress():
            worker = self._from_barack.send_worker()
            if worker:
                work_in_factory = random.randint(1, 5)
                worker.shrink_health(work_in_factory)
                if worker.random_accident_in_fabrik():
                    print('Worker', worker, 'died due an accident!')
                else:
                    self._to_lager.recieve_product(Produkter())
                    self._to_barack.recieve_worker(Arbetare())

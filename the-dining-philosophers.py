class DiningPhilosophers:
    def __init__(self):
        import threading
        self.sem = threading.Semaphore(4)
        self.forks = [threading.Lock() for _ in range(5)]
    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left = philosopher
        right = (philosopher + 1) % 5
        self.sem.acquire()
        self.forks[left].acquire()
        self.forks[right].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.forks[right].release()
        self.forks[left].release()
        self.sem.release()

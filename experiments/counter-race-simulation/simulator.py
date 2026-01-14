import threading
import random
import time

class UserCounter:
    def __init__(self):
        self.count = 0

    def unsafe_update(self, delta):
        temp = self.count
        time.sleep(random.uniform(0.0001, 0.001))
        self.count = temp + delta

    def safe_update(self, delta, lock):
        with lock:
            new_val = self.count + delta
            if new_val < 0:
                return  # reject invalid transition
            self.count = new_val


def run(counter, use_lock=False, iterations=1000):
    lock = threading.Lock()
    failures = 0

    def worker():
        nonlocal failures
        for _ in range(iterations):
            delta = random.choice([1, -1])
            if use_lock:
                counter.safe_update(delta, lock)
            else:
                counter.unsafe_update(delta)

            if counter.count < 0:
                failures += 1

    threads = [threading.Thread(target = worker) for _ in range(10)]
    for t in threads : t.start()
    for t in threads : t.join()

    return failures, counter.count

if __name__ == "__main__":
    print("Running WITHOUT transition invariant...")
    c1 = UserCounter()
    failures1, final1 = run(c1, use_lock=False)
    print("Failures:", failures1, "Final count:", final1)

    print("\nRunning WITH transition invariant...")
    c2 = UserCounter()
    failures2, final2 = run(c2, use_lock=True)
    print("Failures:", failures2, "Final count:", final2)
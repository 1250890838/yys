import threading
lock=threading.Lock()
print(lock.acquire(blocking=True))
print(lock.acquire(blocking=True))
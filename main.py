import threading
from queue import Queue
from domain import *
from gFunctions import *

PROJECT_NAME = "SpiderMan"
HOMEPAGE = ""
DOMAIN_NAME = g_d_n(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + "/q.txt"
CRAWLED_FILE = PROJECT_NAME + "/c.txt"
NUMBER_OF_THREADS = 16
queue = Queue()

def c_w():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=w)
        t.daemon = True
        t.start()
def w():
    while True:
        u = queue.get()
        queue.task_done()
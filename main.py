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
def c_j():
    for l in f_t_s(QUEUE_FILE):
        queue.put(l)
        queue.join()

def c():
    q_l = f_t_s(QUEUE_FILE)
    if len(q_l) > 0:
        print(str(q_l)) + ' links in queue'
        c_j()

        c_w()
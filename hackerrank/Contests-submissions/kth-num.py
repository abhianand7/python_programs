 
import threading

line1 = [int(i) for i in input().split()]

elements = [int(i) for i in input().split()]

class my_thread(threading.Thread):
    def __init__(self, elements,query):
        threading.Thread.__init__(self)
        self.elements = elements
        self.query = query
    def run(self):
        threadLock.acquire()
        result(self.query, self.elements)
        threadLock.release()

def result(query,elements):
    greater_numbers = [i for i in elements if i >= query[0]]
    print (greater_numbers[(query[1]-1)])

threadLock = threading.Lock()
threads = []

for i in range(line1[1]):
    threads.append(my_thread(elements, [int(i) for i in input().split()]))
    threads[i].start()

for t in threads:
    t.join()




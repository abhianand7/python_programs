import threading

line1 = [int(i) for i in input().split()]

elements = [int(i) for i in input().split()]
thread_dict = {}
class my_thread(threading.Thread):
    def __init__(self, elements,query, ID):
        threading.Thread.__init__(self)
        self.elements = elements
        self.query = query
        self.ID = ID
    def run(self):
        result(self.query, self.elements,self.ID)

def result(query,elements,ID):
    greater_numbers = [i for i in elements if i >= query[0]]
    thread_dict[ID] = (greater_numbers[(query[1]-1)])

threads = []

for i in range(line1[1]):
    threads.append(my_thread(elements, [int(i) for i in input().split()], i))
    threads[i].start()

for i in thread_dict:
    print (thread_dict[i])



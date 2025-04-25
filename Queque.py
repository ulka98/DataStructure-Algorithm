from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
        self.size = 0
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        self.size += 1
        return self.buffer

    def dequeue(self):
        if self.size != 0:
            return self.buffer.pop()
            self.size -= 1
        else:
            print("Queue is empty")
            return None
        return None

    def is_Empty(self):
        return self.size == 0
    
    def size(self):
        return self.size
    
    def front(self):
        if not self.buffer.is_empty():
            return self.buffer[-1]
        return None
    
    
## Example usage
pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.size)
print(pq.dequeue())
print(pq.dequeue())


####################EXERCISE 1######################
import threading
import time
import random

'''
Design a food ordering system where your python program will run two threads:
Place Order: This thread will be placing an order and inserting that into a queue. 
This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and
print it. This thread serves an order every 2 seconds. 
Also start this thread 1 second after place order thread is started.
'''

def place_order(orders,queue):
    for i in range(0,len(orders)):
        order = {
            'order_id': i,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'food_item': orders[i],
            'price': random.randint(10, 100)
        }
        queue.enqueue(order)
        print(f"Order placed: {order['food_item']} at {order['timestamp']}")
        time.sleep(0.5)

def serve_order(queue):
    while not queue.is_Empty():
        serving = queue.dequeue()
        print(f"Order served: {serving['food_item']} at {serving['timestamp']}")
        time.sleep(2) # Serves after every 2 seconds

if __name__ == "__main__":
    queue = Queue()

    orders = ['pizza','samosa','pasta','biryani','burger']

    place_order_thread = threading.Thread(target=place_order, args=(orders, queue))
    serve_order_thread = threading.Thread(target=serve_order, args=(queue,))

    place_order_thread.start()
    serve_order_thread.start()

    place_order_thread.join()
    serve_order_thread.join()
    print("All orders have been placed and served.")

####################EXERCISE 2######################
'''Write a program to print binary numbers from 1 to 10 using Queue.'''

def binary_numbers(n):
    binary_numbers_asc = []
    queue = Queue()
    queue.enqueue('1')
    for _ in range(1, n+1):
        s1 = queue.dequeue()
        queue.enqueue(s1 + '0')
        queue.enqueue(s1 + '1')
        binary_numbers_asc.append(int(s1))
    return binary_numbers_asc

if __name__ == "__main__":
    n = 10
    print(f"Binary numbers from 1 to {n}:")
    print("Decimal\tBinary")
    for n, b  in enumerate(binary_numbers(n),1):
        print(f"{n}\t{b}")
    print("All binary numbers have been printed.")

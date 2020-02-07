import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

num = 1
lock = threading.Lock()

def sumarUno():
    global num
    global lock
    try:
        lock.acquire()
        num = num + 1
    finally:
        lock.release()
    

def multiplicarPorDos():
    global num
    global lock
    try:
        lock.acquire()
        num = num * 2
    finally:
        lock.release()
    
    

t1 = threading.Thread(target=sumarUno, name='Sumar 1')
t2 = threading.Thread(target=multiplicarPorDos, name='MultiplicarPorDos')

t2.start()
t1.start()

print(f'Cantidad vale {num}')






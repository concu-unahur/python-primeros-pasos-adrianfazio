import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

num = 1
lock = threading.Lock()

def sumarUno():
    global num
    #global lock
    try
        num += 1
    finally
        lock.release()
   
    

def multiplicarPorDos():
    global num
    global lock
    try:
        lock.acquire()
        num *= 2
    finally:
        lock.release()
    logging.info(f'Cantidad vale {num}')


t1 = threading.Thread(target=sumarUno, name='Sumar 1')
t2 = threading.Thread(target=multiplicarPorDos, name='MultiplicarPorDos')

lock.acquire()

t2.start()
t1.start()

t2.join()
print(f'Cantidad vale {num}')








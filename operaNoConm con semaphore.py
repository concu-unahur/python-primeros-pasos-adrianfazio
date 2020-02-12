import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

num = 1
semaphore = threading.Semaphore(0)

def sumarUno():
    global num
    try:
        num += 1
    finally:
        semaphore.release()
   
    

def multiplicarPorDos():
    global num
    semaphore.acquire()
    try:
        num *= 2
    finally:
        semaphore.release()


t1 = threading.Thread(target=sumarUno, name='Sumar 1')
t2 = threading.Thread(target=multiplicarPorDos, name='MultiplicarPorDos')


t2.start()
t1.start()

t2.join()
print(f'Cantidad vale {num}')








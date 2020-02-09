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

def unoDivididoDos():
    global num
    num = 1/2

def tresDivididoDos():
    global num
    num = 3/2

def primeraCuenta():
    global num
    tprimero = threading.Thread(target=sumarUno)
    tprimero.start()
    tprimero.join()
    tprimero.start()
    tprimero.join()
    tprimero.start()
    tprimero.join()
    print(f'Cantidad vale {num}')


t1 = threading.Thread(target=sumarUno, name='Sumar 1')
t2 = threading.Thread(target=multiplicarPorDos, name='MultiplicarPorDos')
t3 = threading.Thread(target=unoDivididoDos, name='unoDivididoDos')
t4 = threading.Thread(target=tresDivididoDos, name='tresDivididoDos')
t5 = threading.Thread(target=primeraCuenta)

#t2.start()
#t1.start()
#t3.start()
#t4.start()
t5.start()

print(f'Cantidad vale {num}')







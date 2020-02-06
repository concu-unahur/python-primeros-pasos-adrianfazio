import threading
import time
import logging
from tiempo import Contador



logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


# la función para usar para el thread
def dormir(secs):
    time.sleep(secs)

contador = Contador()
contador.iniciar()
lista = [] #crea una lista vacia

for i in range(10):
    #crear un thead
    t = threading.Thread(target=dormir, name='thread 1', args=[2])
    logging.info('Thread ')

    #lanzarlo
    t.start()
    lista.append(t)
    # t.join()

for thread in lista:
    thread.join()

contador.finalizar()
contador.imprimir()




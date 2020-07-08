import socket
from concurrent.futures import ProcessPoolExecutor

#Will create an online such that one can use the somethingsomething soemthing.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234)) #Uses uft-8 standards
server.listen(5)
"""
with ProcessPoolExecutor() as executor:
    pass
"""

while True:
    clientsocket, adress = server.accept()
    print(f'Connection with {adress} have been established.')

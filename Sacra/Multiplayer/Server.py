import socket
from concurrent.futures import ProcessPoolExecutor

#Will create an online such that one can use the somethingsomething something.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234)) #Uses uft-8 standards
server.listen(5)
"""
with ProcessPoolExecutor() as executor:
    pass
"""

while True:
    clientsocket, address = server.accept()
    print(f'Connection with {address} have been established.')

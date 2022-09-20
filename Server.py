import socket
import threading
import time

host = "10.4.1.219"
port = 7778

def thread_function(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(addr + data)
            conn.send()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(3)
    while True:
        conn, addr = s.accept()
        my_thread = threading.Thread(target=thread_function, args=(conn, addr))
        my_thread.start()




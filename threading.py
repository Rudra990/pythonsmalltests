import threading

def print_hello():
    print('Hello from thread!')
thread = threading.Thread(target=print_hello)
thread.start()
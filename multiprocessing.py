import multiprocessing

def print_square(n):
    print(n * n)
process = multiprocessing.Process(target=print_square, args=(4,))
process.start()
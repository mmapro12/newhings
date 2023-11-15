from time import time

def speedTest(func):
    def wrapper():
        start = time()
        func()
        end = time()

        print(f"Function time: {end-start}")
    
    return wrapper


@speedTest
def func():
    print("Hello every one como estas?")

func()
from threading import Timer

def hello():
    print("hello, world")
    Timer(1.0, hello).start()

Timer(1.0, hello).start()
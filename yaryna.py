def cycle(iterable):
    while True:
        for element in iterable:
            yield element

def repeat(value):
    while True:
        yield value
        
def count(start=0, step=1):
    i = 0
    while True:
        yield start + i*step
        i += 1

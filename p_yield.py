'''
def h():
    print("hello")
    yield 5

c = h()
c.__next__()
'''

def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 3
    print("step 3")
    yield 5

o = odd()
o.__next__()


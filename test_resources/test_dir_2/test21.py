class Test21(object):
    def __init__(self):
        self.counter = 0
    
    def increment(self):
        self.counter += 1

test = Test21()
for i in range(10):
    test.increment()

# TODO: write some docs on what this is for
print(test)
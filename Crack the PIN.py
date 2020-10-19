import hashlib
# don't print anything in the console, because it will take to much time
def crack(hash):
    for i in range(100000):
        pin  = "{:05d}".format(i)
        if hashlib.md5(pin.encode()).hexdigest() == hash:
            return pin

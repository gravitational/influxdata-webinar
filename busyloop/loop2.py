from threading import Thread

def loop():
    while True:
        pass

if __name__ == "__main__":
    threads = []
    for i in range (0, 2):
        print "starting thread %d" % (i, )
        t = Thread(target=loop)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()



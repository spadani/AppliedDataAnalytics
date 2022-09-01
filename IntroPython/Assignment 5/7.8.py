import time


class Stopwatch:

    def __init__(self):
        self.starttime = time.time()
        self.endtime = None


    def getstarttime(self):
        return self.starttime

    def getendtime(self):
        return self.endtime

    def start(self):
        self.starttime = time.time()

    def stop(self):
        self.endtime = time.time()

    def getelapsedtime(self):
        return (self.getendtime() - self.getstarttime()) * 1000


def main():
    stopwatch = Stopwatch()
    total = 0
    for i in range(1, 1000000):
        total += i
    stopwatch.stop()
    exectime = stopwatch.getelapsedtime()
    print(exectime, "milliseconds")


main()











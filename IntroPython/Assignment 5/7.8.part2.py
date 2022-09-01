import time


class Stopwatch:

    INITIAL = 0
    RUNNING = 1
    STOP = 2

    def __init__(self):
        self.starttime = time.time()
        self.endtime = None
        self.state = Stopwatch.INITIAL

    def getstate(self):
        return self.state

    def setstate(self, state):
        self.state = state

    def getstarttime(self):
        return self.starttime

    def getendtime(self):
        return self.endtime

    def start(self):
        if self.getstate() != Stopwatch.STOP:
            self.starttime = time.time()
        self.setstate(Stopwatch.RUNNING)

    def stop(self):
        self.endtime = time.time()
        self.setstate(Stopwatch.STOP)

    def reset(self):
        self.setstate(Stopwatch.INITIAL)

    def getelapsedtime(self):
        if self.getstate() == Stopwatch.INITIAL:
            return 0
        elif self.getstate() == Stopwatch.RUNNING:
            return (time.time() - self.getstarttime()) * 1000
        else:
            return (self.getendtime() - self.getstarttime()) * 1000


def main():
    stopwatch = Stopwatch()
    stopwatch.start()
    time.sleep(.2)
    stopwatch.stop()
    exectime = stopwatch.getelapsedtime()
    # 200ms
    print(exectime, "ms")
    stopwatch.reset()
    stopwatch.start()
    time.sleep(.2)
    exectime = stopwatch.getelapsedtime()
    # 200ms
    print(exectime, "ms")
    time.sleep(.5)
    exectime = stopwatch.getelapsedtime()
    # 700ms
    print(exectime, "ms")
    stopwatch.stop()
    stopwatch.start()
    time.sleep(.3)
    stopwatch.stop()
    exectime = stopwatch.getelapsedtime()
    # 1s
    print(exectime, "ms")


main()


